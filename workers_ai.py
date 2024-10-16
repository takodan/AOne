# Cloudflare Workers AI REST API
import requests
import hidden
import base64
from PIL import Image
import numpy as np
import torchvision.transforms as transforms

ACCOUNT_ID = hidden.cloudflare_ai_api_account_id()
AUTH_TOKEN = hidden.cloudflare_ai_api_token()

API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"

def initialize_llama():
    response = requests.post(
        f"{API_BASE_URL}@cf/meta/llama-3.2-11b-vision-instruct",
        headers = {"Authorization": f"Bearer {AUTH_TOKEN}"},
        json = { "prompt": "agree"}
    )
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return result

def read_image_binary(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
def read_image_array(image_path):
    with Image.open(image_path) as image_file:
        image = image_file.convert('L')
        image_array = np.array(image)
        image_array_flat = image_array.flatten().tolist()
        return image_array_flat

def read_image_tensor(image_path):
    with Image.open(image_path) as image_file:
        image = image_file.convert('L')
        transform = transforms.Compose([transforms.PILToTensor()])
        img_tensor = transform(image)
        array_tensor = img_tensor.flatten().tolist()
        return array_tensor

def receipt_ocr(model, image_data):
    print(type(image_data))
    # post
    response = requests.post(
        f"{API_BASE_URL}{model}",
        headers = {"Authorization": f"Bearer {AUTH_TOKEN}"},
        json = {
            "messages": [
                {"role": "system", "content": "You output a JSON object that includes receipt details such as store name, date, purchased items."},
                {"role": "user", "content": "Give me the store name"},
                {"role": "assistant", "content": "{\"store_name\":\"Trader Joe\'s\"}"},
                {"role": "user", "content": "Give me the store name from this picture"},
                # {"role": "assistant", "content": ""}
            ],
            "image": image_data,
        }
    )

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return  


def receipt_ocr_prompt_only(model, image_data):
    print(type(image_data))
    # post
    response = requests.post(
        f"{API_BASE_URL}{model}",
        headers = {"Authorization": f"Bearer {AUTH_TOKEN}"},
        json = {
            "prompt": "Give me the store name from this picture",
            "image": image_data,
        }
    )

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return  


def cat_prompt_only(model, image_data):
    print(type(image_data))
    # post
    response = requests.post(
        f"{API_BASE_URL}{model}",
        headers = {"Authorization": f"Bearer {AUTH_TOKEN}"},
        json = {
            "prompt": "What's the animal in the picture?",
            "image": image_data,
        }
    )

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code}, Message: {response.text}")
        with open("workersAI.txt", "a") as f:
            f.write(response.text)
        return "Error!"


if __name__ == "__main__":
    
    # modules
    # initialize_llama()
    # @cf/meta/llama-3.2-11b-vision-instruct
    # @cf/meta/llama-3.2-3b-instruct


    # read image
    # im = read_image_binary(r"cat.png")
    # im = read_image_array(r"cat.png")
    im = read_image_tensor(r"cat.png")

    # orc receipt
    # output = receipt_ocr("@cf/meta/llama-3.2-11b-vision-instruct", im)
    # output = receipt_ocr_prompt_only("@cf/meta/llama-3.2-11b-vision-instruct", im)
    output = cat_prompt_only("@cf/meta/llama-3.2-11b-vision-instruct", im)

    print(output)
