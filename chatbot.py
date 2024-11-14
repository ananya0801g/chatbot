import openai

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the chatbot's reply from the response
    reply = response['choices'][0]['message']['content']
    return reply

# Chat loop
print("Chatbot: Hello! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chat_with_gpt(user_input)
    print("Chatbot:", response)
