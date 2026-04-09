# src/core/llm_client.py
import requests
from src.utils.logger import logger
from src.models.error_codes import ErrorCode
from src.utils.exceptions import LLMError
from src.models.config_schema import LLMConfig

class LLMClientFactory:
    """根据配置创建具体的 LLM 实例"""
    @staticmethod
    def create(config: LLMConfig):
        if config.mode == "cloud":
            return CloudLLMClient(config)
        return OllamaClient(config)

class BaseLLMClient:
    def __init__(self, config: LLMConfig):
        self.cfg = config

    def _parse_answer(self, text: str) -> str:
        text = text.upper()
        for char in reversed(text):
            if char in "ABCD": return char
        return "N/A"

class OllamaClient(BaseLLMClient):
    def ask(self, q_data: dict) -> str:
        # 1. 提取 OCR 数据
        context_parts = [f"Topic: {q_data.get('topic', '')}"]
        for opt in "ABCD":
            if q_data.get(opt):
                context_parts.append(f"{opt}: {q_data[opt]}")
        context = "\n".join(context_parts)

        # 2. 获取模板并进行填充
        # 注意：这里的 self.cfg.prompt_template 如果是 "You are an English..." 
        # 说明外部传进来的配置根本没生效！
        template = self.cfg.prompt_template
        full_prompt = template.format(context=context)

        # ==================== [ 强力 DEBUG 输出 ] ====================
        print("\n" + "🔥" * 30)
        print("【提示词加载逻辑监控】")
        
        # 判断提示词来源
        if "English Exam Expert" in template:
            print("❌ 警告：当前正在使用 [代码内置默认模板]，configs.json 未生效！")
        else:
            print("✅ 成功：当前正在使用 [外部自定义模板]")
        
        # ============================================================

        # ... 后面是原来的 requests 逻辑 ...
        
        payload = {
            "model": self.cfg.model_name,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": self.cfg.temperature,
                "num_predict": self.cfg.max_tokens
            }
        }
        try:
            r = requests.post(self.cfg.api_url, json=payload, timeout=self.cfg.timeout)
            r.raise_for_status()
            return self._parse_answer(r.json().get('response', ""))
        except Exception as e:
            raise LLMError(ErrorCode.LLM_CONN_ERROR, detail=str(e))
    @staticmethod
    def fetch_all_models():
        """
        静态方法：不需要实例化类就能调用。
        调用方式：OllamaClient.fetch_all_models()
        """
        try:
            import requests
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            if response.status_code == 200:
                return [m['name'] for m in response.json().get('models', [])]
        except:
            pass
        return ["None"] # 保底


class CloudLLMClient(BaseLLMClient):
    def ask(self, q_data: dict) -> str:
        headers = {"Authorization": f"Bearer {self.cfg.api_key}"}
        context = f"Topic:{q_data.get('topic')}..."
        full_prompt = self.cfg.prompt_template.format(context=context)
        
        payload = {
            "model": self.cfg.model_name,
            "messages": [{"role": "user", "content": full_prompt}],
            "temperature": self.cfg.temperature,
            "max_tokens": self.cfg.max_tokens
        }
        try:
            # 云端 API 路径通常需要补全 /v1/chat/completions
            url = self.cfg.api_url.rstrip('/') + "/chat/completions"
            r = requests.post(url, json=payload, headers=headers, timeout=self.cfg.timeout)
            r.raise_for_status()
            res = r.json()['choices'][0]['message']['content']
            return self._parse_answer(res)
        except Exception as e:
            raise LLMError(ErrorCode.LLM_CONN_ERROR, detail=str(e))