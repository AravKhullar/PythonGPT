import openai
from flask import Flask, render_template, request, jsonify
from main import chat_with_gpt, chat_history  # Import from main.py

# OpenAI API key (ensure you are not sharing this key in public repositories)
openai.api_key = "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"

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
