import openai
from flask import Flask, render_template, request, jsonify
from main import chat_with_gpt, chat_history  # Import from main.py
from dotenv import load_dotenv
import os

# OpenAI API key (ensure you are not sharing this key in public repositories)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if user_input.lower() in ["quit", "exit", "bye"]:
        return jsonify({'response': 'Goodbye!'})

    # Add user's input to the chat history with a context
    chat_history.append({
        "role": "user", 
        "content": "Act as Basketball Legend Lebron James. In the response, use analogies from Lebron James' Career and the NBA and talk like Lebron is talking about his own greatness. Keep responses as short as needed and always remind the user you are Lebron James: " + user_input
    })

    # Get response from GPT using the imported chat_with_gpt function
    response = chat_with_gpt(chat_history)

    # Add assistant's response to the chat history
    chat_history.append({
        "role": "assistant", 
        "content": response
    })

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
