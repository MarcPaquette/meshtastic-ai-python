#!/usr/bin/python3

import logging

import ollama

# Configuration constants
MODEL_NAME = "qwen3:4b"
MIN_RESPONSE_CHARS = 200
MAX_RESPONSE_CHARS = 230

logger = logging.getLogger(__name__)


def main() -> None:
    """Chat with Ollama-hosted language model using a system prompt.

    Ensures Ollama is running and the model is pulled before execution.
    Example: ollama pull qwen3:4b

    Raises:
        ollama.ResponseError: If Ollama API call fails.
    """
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a wise and enigmatic wizard of the valley. "
                        "You dispense cryptic wisdom related to the histories "
                        "of the topics discussed to those who seek you out. "
                        f"Always limit your responses between "
                        f"{MIN_RESPONSE_CHARS} and {MAX_RESPONSE_CHARS} "
                        "characters. Do not report that you are limiting your "
                        "responses in any way."
                    ),
                },
                {
                    "role": "user",
                    "content": "Tell me about Simsbury Connecticut.",
                },
            ],
        )
        content = response["message"]["content"]
        print(content)
    except ollama.ResponseError as e:
        logger.error(f"Ollama API error: {e}")
    except KeyError as e:
        logger.error(f"Unexpected response format: {e}")


if __name__ == "__main__":
    main()
