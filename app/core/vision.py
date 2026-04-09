import os
import re
import easyocr
import numpy as np
from app.core.path_utils import get_bin_path

class VisionSystem:
    def __init__(self, use_gpu=True):
        print("正在初始化 EasyOCR 视觉引擎")
        model_dir = get_bin_path("models") 
        self.reader = easyocr.Reader(['en', 'ch_sim'], 
                                     gpu=use_gpu, 
                                     model_storage_directory=model_dir)
        if not os.path.exists('debug'):
            os.makedirs('debug')

    def process_rois(self, full_img, roi_config):
        """
        批量处理图像区域，返回清洗后的字典
        """
        q_data = {}
        for key, box in roi_config.items():
            # 绝对坐标切割
            roi_img = full_img.crop((box[0], box[1], box[2], box[3]))
            roi_img.save(f"debug/roi_{key}.png")
            
            # OCR 识别
            result = self.reader.readtext(np.array(roi_img), detail=0)
            text = " ".join(result).strip()
            
            # 强力格式清洗
            if key in "ABCD":
                content = re.sub(rf'^[A-D0@\s\._]+', '', text, flags=re.I)
                text = f"{key}: {content}"
                
            q_data[key] = text
            print(f"  {text}")
            
        return q_data