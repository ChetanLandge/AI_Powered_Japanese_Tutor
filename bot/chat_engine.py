import openai
import os

# Load your OpenAI API key from environment
openai.api_key = os.getenv("API_KEY")

def get_gpt_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Japanese tutor. For any English input:\n"
                        "- Translate it into Japanese with romaji.\n"
                        "- List all vocabulary including: kanji, hiragana/katakana, romaji, and English meaning.\n"
                        "- Explain grammar and particles used in the sentence.\n"
                        "- Give one similar use case of the grammar.\n"
                        "- Provide one example sentence in Japanese with translation.\n"
                        "- Make the answer visually appealing using emojis or symbols."
                    )
                },
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']

    except Exception as e:
        print("❌ GPT Error:", str(e))
        return "Sorry, something went wrong. 😓"
