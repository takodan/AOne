# pip install Pillow
# pip install pillow-heif

from PIL import Image
import numpy as np
import cv2
import pillow_heif
import os


def heic_to_png(image_path):
    heic_name = os.path.basename(image_path)
    print(f"{heic_name=}")
    png_name = heic_name.replace("HEIC", "png")
    print(f"{png_name=}")

    im = pillow_heif.open_heif(image_path, convert_hdr_to_8bit=False, bgr_mode=True)
    np_array = np.asarray(im)
    cv2.imwrite(f"receipt_image\{png_name}", np_array)

    with Image.open(f"receipt_image\{png_name}") as png_im:
        png_im.thumbnail((320, 320))
        png_im.save(f"receipt_image\{png_name}", 'PNG', optimize=True )


def png_to_webp(image_path):
    png_name = os.path.basename(image_path)
    webp_name = png_name.replace("png", "webp")
    with Image.open(image_path) as im:
        im.save(f"{webp_name}", 'WebP', quality=60, )

def png_to_jpeg(image_path):
    png_name = os.path.basename(image_path)
    jpeg_name = png_name.replace("png", "jpg")
    with Image.open(image_path) as im:
        im.save(f"{jpeg_name}", 'JPEG')
        

def png_to_png_gray_scale(image_path):
    png_name = os.path.basename(image_path)
    gray_name = png_name.replace(".png", "_gray.png")
    with Image.open(image_path) as im:
        im = im.convert('L')
        im.save(f"{gray_name}", 'PNG')



if __name__ == "__main__":
    heic_to_png(r"C:\danny\2_code\2_repo\AOne\receipt_image\IMG_0641.HEIC")
    # png_to_webp(r"C:\danny\2_code\2_repo\AOne\receipt_image\IMG_0641.png")
    # png_to_jpeg(r"C:\danny\2_code\2_repo\AOne\receipt_image\IMG_0641.png")

    # input_image_path = input("Enter the image path: ")
    # fun = input("Enter a number to select function:\n\
    #         1 HEIC to png\n")
    
    # if fun == "1":
    #     heic_to_png(input_image_path)