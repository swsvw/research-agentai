from groq import Groq


# Creates a Groq client with the user's API key
def get_groq_client(api_key: str):
    return Groq(api_key=api_key)

# Calls the Groq model using the provided prompt and client
def groq_llm(prompt: str, client):
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content.strip()

