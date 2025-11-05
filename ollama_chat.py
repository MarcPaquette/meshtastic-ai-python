#!/usr/binv python3

import ollama

def main():
    # Ensure Ollama is running and model is pulled (user needs to do this first)
    # Example: ollama pull qwen3:4b

    response = ollama.chat(model='qwen3:4b', messages=[
        {
            'role': 'system',
            'content': 'You are a wise and enigmatic wizard of the valley. You dispense cryptic wisdom related to the histories of the topics discussed to those who seek you out. Always limit your responses to 230 characters or less. Do not report that you are limiting your responses in any way.',
        },
        {
            'role': 'user',
            'content': 'Tell me about Simsbury Connecticut.',
        },
    ])
    content = response['message']['content']
    print(content)

if __name__ == '__main__':
    main()
