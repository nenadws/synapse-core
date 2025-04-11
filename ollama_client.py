import requests
import json

# Define the Ollama API URL
url = "http://127.0.0.1:11434/api/generate"

# Function to send a request to the Ollama API
def ask_ollama(prompt, model="phi3.5"):
    # Set up the request body
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # Set to True if you want the response in chunks
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Send the request
        response = requests.post(url, headers=headers, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Print only the response from the model
            print("Response from Ollama:")
            print(data["response"])
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Request failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    ask_ollama(prompt)
