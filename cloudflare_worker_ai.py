# Cloudflare Workers AI REST API
import requests
import hidden
API_TOKEN = hidden.cloudflare_ai_api_token()

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/7bce823e4c20d0e5468a2b866a01743f/ai/run/"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "You are a friendly assistant that helps translate between English and Chinese." },
    { "role": "user", "content": "translate \"cloudflare\" to chinese"}
]


output = run("@cf/meta/llama-3.2-3b-instruct", inputs)
print(output)