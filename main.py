from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# ✅ Replace with your OpenAI API key
OPENAI_API_KEY = "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"

@app.route("/", methods=["GET"])
def home():
    return "ChatGPT Webhook is running!"

@app.route("/chatgpt", methods=["POST"])
def chat():
    data = request.get_json()
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "No query received"}), 400

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_query}],
        api_key=OPENAI_API_KEY
    )

    ai_response = response["choices"][0]["message"]["content"]
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # ✅ Use port 10000 for Render
