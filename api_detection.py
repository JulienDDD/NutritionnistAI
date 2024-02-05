import os
import openai 
import base64

openai.api_key = ""
def process_image(file_path):
    try:
        with open(file_path, 'rb') as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
            return image_base64
    except FileNotFoundError:
        print(f"Fichier {file_path} introuvable.")
        return None

def analyze_image(image_base64):
    if image_base64:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Qui a t'il dans ce frigo ?"},
                            {
                                "type": "image_url",
                                "image_url": "https://i.pinimg.com/originals/1d/88/94/1d889403191556416a7097b8ed44b700.jpg",
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )
            print(response.choices[0].message.content)
        except openai.error.OpenAIError as e:
            print(f"Erreur OpenAI : {e}")


if __name__ == "__main__":
    image_path = "input.jpg"
    image_base64 = process_image(image_path)
    analyze_image(image_base64)
