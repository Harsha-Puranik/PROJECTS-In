def my_chatboat_assistant():
    print("Chatbot: Hey there! I am your friendly assistant.")
    print("Chatbot: How can I help you today?")
    print("You can try saying: hello, how are you, bye.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello":    
            print("Chatbot: Hello! Nice to see you 😊")
        elif user_input == "how are you": 
            print("Chatbot: I am doing great! Thanks for asking ✨")
        elif user_input == "bye":
            print("Chatbot: See you later! 👋")
            break
        else:
            print("Chatbot: Sorry, I didn’t get that. Please try again.")

# Start the assistant
my_chatboat_assistant()
