import openai

# 🚨 کلید حساس — مراقب باش فقط توی سیستم خودت استفاده شه
openai.api_key = "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"

# 🧠 حافظه گفت‌وگو برای مکالمه پایدار
chat_history = [
    {
        "role": "system",
        "content": (
            "You are Begail, an intelligent assistant created by Mohammad Begail. "
            "Your personality is helpful, witty, and loyal. Always introduce yourself as Begail. "
            "Speak fluently in both Persian and English when needed."
        )
    }
]

# 💬 تابع مکالمه با Begail
def ask_begail(question):
    chat_history.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    reply = response['choices'][0]['message']['content']
    chat_history.append({"role": "assistant", "content": reply})
    return reply

# 🧪 اجرای چت‌بات در ترمینال
if __name__ == "__main__":
    print("🔷 Chat with Begail started. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            print("Begail: Goodbye, my friend. ✨")
            break
        response = ask_begail(user_input)
        print(f"Begail: {response}\n")
