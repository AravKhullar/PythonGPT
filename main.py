import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages = chat_history
    )

    return response.choices[0].message.content.strip()
chat_history = []
if __name__ == "__main__":
    while True:
        user_input = input('You: ')
        
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        chat_history.append({"role" : "user", "content" : user_input})
        response = chat_with_gpt(chat_history)
        print("Chatbot: ", response)
        chat_history.append({"role" : "assistant", "content" : response})