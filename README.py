# gemini-clone
import google.generativeai as genai

API_KEY ="AIzaSyBnmMoJRWqivBZsz5qayPk1rNsjbqrcjz4"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print('Chat with gemini type "Exit" to quit')
while True:
    user_input =input("You: ")
    if user_input.lower() == 'exit' and 'Exit' :
        break
    response = chat.send_message(user_input)
    print("Gemini",response.text)
