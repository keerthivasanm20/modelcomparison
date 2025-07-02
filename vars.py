import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
PROMPTS = {
    "appdev": "Generate a Python function that parses a JSON file and stores its content in a PostgreSQL database.",
    "data": "Write an SQL query to find the top 5 customers by revenue from a sales table with columns: customer_id, sale_amount, sale_date.",
    "devops": "Write a bash script that installs Docker, starts a service, and opens the correct firewall ports.",
}