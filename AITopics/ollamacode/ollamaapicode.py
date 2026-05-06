import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = '{\n  "model": "qwen3-vl:8b",\n  "prompt": "Why is the sky blue?"\n}'

response = requests.post('http://localhost:11434/api/generate', headers=headers, data=data)

print(response.text)