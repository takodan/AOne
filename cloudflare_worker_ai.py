# Cloudflare Workers AI REST API
import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/7bce823e4c20d0e5468a2b866a01743f/ai/run/"
headers = {"Authorization": "Bearer e201I3O212ISYPWSek2CEHiMGYcX_O4iMDQ203wk"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud "}
]


output = run("@cf/meta/llama-3.2-3b-instruct", inputs)
print(output)