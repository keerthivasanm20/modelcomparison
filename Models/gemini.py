import google.generativeai as genai
import vars

def call_gemini(prompt):
    try:
        genai.configure(api_key=vars.GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error with Gemini: {e}"