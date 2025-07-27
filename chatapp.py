def chatbot():
    print("Simple Chatbot: Type 'exit' to end.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        elif user_input == "exit":
            print("Bot: Exiting chat.")
            break
        else:
            print("Bot: I don't understand.")

chatbot()
