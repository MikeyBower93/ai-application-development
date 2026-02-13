import requests

url = 'https://api.openai.com/v1/chat/completions'
api_key = ''
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
data = {
    'model': 'gpt-4o-mini',
    'messages': [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'What do you think are the most important inventions of the 21st century?'},
    ],
    'temperature': 0.7
}

response = requests.post(url, headers=headers, json=data)

try:
    response.raise_for_status()
    reply = response.json()['choices'][0]['message']['content']
    print(reply)
except requests.exceptions.HTTPError as http_error:
    print(http_error)
except Exception as e:
    print(e)
