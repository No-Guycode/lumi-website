from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY") 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    user_input = request.form.get("prompt")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=f"user: {user_input}\nAI:",
            max_tokens=1024, 
            n=1, 
            stop=None, 
            temperature=0.7,
        )
        ai_response = response.choices[0].text.strip()
    except Exception as e: 
        ai_response = f"Error: {e}" 
    return {"response": ai_response}

if __name__ == "__main__":
    app.run(debug=True)
