import requests


def unload_ollama_model(model_name: str, base_url: str = "http://localhost:11434") -> bool:
    """Utility function to forcefully unload any Ollama model from VRAM/RAM.

    Args:
        model_name (str): The name of the model to unload .
        base_url (str): The base URL where Ollama is running.

    Returns:
        bool: True if successfully unloaded, False otherwise.
    """
    print(f"Unloading model '{model_name}' from memory...")

    try:
        response = requests.post(
            f"{base_url}/api/generate",
            json={
                "model": model_name,
                "prompt": "",  # Required to trigger model cleanup cleanly
                "keep_alive": 0
            },
            timeout=10
        )

        if response.status_code == 200:
            print(f"Model '{model_name}' successfully unloaded from memory.")
            return True
        else:
            print(f"Failed to unload model '{model_name}'. Status: {response.status_code}, Response: {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Failed to communicate with Ollama server at {base_url}: {e}")
        return False