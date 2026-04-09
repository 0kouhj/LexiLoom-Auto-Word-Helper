import requests

class LLMClient:
    def __init__(self, url="http://localhost:11434/api/generate", model_name="qwen2.5:7b"):
        self.url = url
        self.model_name = model_name

    def get_answer(self, q_data):
        context = f"Topic:{q_data['topic']}\nA:{q_data['A']}\nB:{q_data['B']}\nC:{q_data['C']}\nD:{q_data['D']}"
        prompt = f"""You are an English Exam Expert. 
        Task: Find the BEST synonym or translation for the Topic.
        ---
        Question:
        {context}
        ---
        Rules:
        1. ONLY output the single letter (A, B, C, or D).
        2. If multiple options are close, choose the most professional and precise one.
        3. Ignore OCR noise like '@', '_', or '.'.
        Answer: """

        try:
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 6,
                    "temperature": 0.0
                }
            }
            r = requests.post(self.url, json=payload, timeout=5)
            res = r.json().get('response', "").upper()
            
            # 倒序查找防废话
            for char in reversed(res):
                if char in "ABCD":
                    return char
            return None
        except Exception as e:
            print(f"❌ 大模型推理异常: {e}")
            return None