import Models.claude
import Models.gemini
import Models.gpt
import Models.ollama
import vars
import Models
def compare_models():
    results = {}

    for task, prompt in vars.PROMPTS.items():
        results[task] = {
            "GPT-4o": Models.gpt.call_openai(prompt),
            "Claude Sonnet": Models.claude.call_claude(prompt),
            "Gemini Flash": Models.gemini.call_gemini(prompt),
            "DeepSeek-R1:7B (Local)": Models.ollama.call_ollama(prompt),
        }

        for model, output in results[task].items():
            print(f"\n--- {model} ---\n{output}\n")
        breakpoint()
    return results


if __name__ == "__main__":
    compare_models()