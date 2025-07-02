import openai
import vars

def call_openai(prompt):
    openai.api_key = vars.OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error with OpenAI: {e}"