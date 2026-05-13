import os
import requests

headers = {
    'Authorization': 'Bearer ' + os.getenv('LM_API_TOKEN', ''),
    'Content-Type': 'application/json',
}

json_data = {
    'model': 'microsoft/phi-4-mini-reasoning',
    'input': 'Tell me the top trending model on hugging face and navigate to https://lmstudio.ai',
    'context_length': 8000,
    'temperature': 0,
}

response = requests.post('http://localhost:1234/api/v1/chat', headers=headers, json=json_data)

print(response.content)