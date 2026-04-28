import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCoJ5Iyr3QYdiZqcf3FNafzm8PpAOGpb58")
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")
chat = model.start_chat(history=[])
print("Keer's (Type 'exit' to quit)")
print("welcome, how can i help you?")
while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit","quit","bye"]:
        break
    response = chat.send_message(user_input)
    print(f"Idealabs:{response.text}")
