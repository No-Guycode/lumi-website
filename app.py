from flask import Flask, render_template, request
import openai

openai.api_key = "OPENAI_API_KEY"

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
  user_input = request.form["user_input"]
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"user: {user_input}\nAI:",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
  )
  return render_template("index.html", user_input=user_input, ai_response=response.choices[0].text.strip())

if __name__ == "__main__":
  app.run(debug=True)
