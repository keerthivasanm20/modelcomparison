import requests
import vars
import json

# def call_ollama(prompt, model="deepseek-r1:7b"):
#     try:
#         print('Calling Ollama API...')
#         print(f"Using model: {model}")
#         print(f"Prompt: {prompt}")
#         response = requests.post(
#             f"{vars.OLLAMA_HOST}/api/chat",
#             json={
#                 "model": model,
#                 "messages": [{"role": "user", "content": prompt}]
#             }
#         )
#         print(f"Response status code: {response.status_code}")
#         print(f"Response content: {response}")
#         breakpoint()
#         if response.status_code != 200:
#             return f"Error: Received status code {response.status_code} from Ollama API"
#         return response.json()
#     except Exception as e:
        # return f"Error with Ollama: {e}"

def call_ollama(prompt, model="deepseek-r1:7b"):
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "stream": True
            },
            stream=True
        )

        output = ""
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                output += chunk.get("message", {}).get("content", "")
        return output
    except Exception as e:
        return f"Error with Ollama (streaming): {e}"