# import easyocr

# reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

# input_image_path = input("Enter the image path: ")
# result = reader.readtext(input_image_path)

# with open("orc.txt", 'w', encoding='utf-8') as f:
#     for (bbox, text, prob) in result:
#         f.write(text + '\n')


import numpy as np
from PIL import Image, ImageEnhance
import easyocr

def preprocess_image(image_path, output_path):
    # 使用 Pillow 打開圖片
    img = Image.open(image_path)

    # 調整對比度
    enhancer = ImageEnhance.Contrast(img)
    img_enhanced = enhancer.enhance(2)  # 調高對比度，2 是對比度倍數，可以根據情況調整

    # 將圖片轉為灰度
    img_gray = img_enhanced.convert('L')

    # 保存灰度圖片以便觀察效果
    img_gray.save(output_path + "_gray.png")

    return output_path + "_gray.png"

    # # 將灰度圖片轉換為 NumPy 數組以便進行進一步處理
    # img_np = np.array(img_gray)

    # # 使用 OpenCV 進行二值化處理
    # _, img_binary = cv2.threshold(img_np, 50, 255, cv2.THRESH_BINARY)  # 150 是閾值，根據需要調整

    # # 保存處理後的圖片
    # cv2.imwrite(output_path + "_binary.png", img_binary)

    # # 返回處理後的圖片路徑
    # return output_path + "_binary.png"

def ocr_image_with_preprocessing(image_path, output_txt_path, languages=['en']):
    # 預處理圖片
    processed_image_path = preprocess_image(image_path, "processed_image")

    # 初始化 OCR 閱讀器
    reader = easyocr.Reader(languages)
    
    # 讀取並解析處理後的圖像文本
    result = reader.readtext(processed_image_path)
    
    # 打開一個 txt 文件，準備寫入解析出的文字
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        for (bbox, text, prob) in result:
            f.write(text + '\n')
    
    print(f"OCR results after preprocessing have been written to {output_txt_path}")

# 範例使用
image_path = r"receipt_image\IMG_0641.png"  # 原始圖片文件路徑
output_txt_path = r"orc.txt"  # 保存的 txt 文件路徑
ocr_image_with_preprocessing(image_path, output_txt_path, languages=['en'])
