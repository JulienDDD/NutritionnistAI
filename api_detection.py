import os
import openai 
import base64
import json

openai.api_key = "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"

def process_image(file_path):
    try:
        with open(file_path, 'rb') as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
            return image_base64
    except FileNotFoundError:
        print(f"Fichier {file_path} introuvable.")
        return None

def analyze_image():
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Qui a t'il dans ce frigo ? analyse tout les ingredients et genere la recette la plus adaptée aux aliments presents"},
                            {
                                "type": "image_url",
                                "image_url": "https://i.pinimg.com/originals/1d/88/94/1d889403191556416a7097b8ed44b700.jpg",
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )

            content = response.choices[0].message.content

            print(content)
        except openai.error.OpenAIError as e:
            print(f"Erreur OpenAI : {e}")

if __name__ == "__main__":
 
    analyze_image()
