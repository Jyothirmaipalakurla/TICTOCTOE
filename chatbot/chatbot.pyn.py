def recommend_movie(genre):
    if genre == "action":
        print("Chatbot: I recommend watching 'Mission Impossible.'")
    elif genre == "comedy":
        print("Chatbot: I recommend watching 'Dumb and Dumber.'")
    elif genre == "drama":
        print("Chatbot: I recommend watching 'The Shawshank Redemption.'")
    else:
        print("Chatbot: I'm sorry, I don't have a recommendation for that genre.")

def provide_information():
    print("Chatbot: I am a rule-based chatbot designed for simple interactions. I can provide information on various topics, answer questions, and engage in casual conversation.")

def process_feedback(rating):
    if rating >= 4:
        print("Chatbot: Thank you for your positive feedback! I'm here to help whenever you need assistance.")
    elif rating >= 2:
        print("Chatbot: Thank you for your feedback. I'll strive to improve. If you have any specific suggestions, please let me know!")
    else:
        print("Chatbot: We're sorry to hear that you didn't have a great experience. Please provide more details on how we can improve.")

def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input().lower()
        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you?":
            print("Chatbot: I'm good, thank you. How about you?")
        elif user_input == "good name please":
            print("Chatbot: I'm known as 'ai'.")
        elif user_input == "what can you do?":
            print("Chatbot: I can help answer questions, provide information, recommend movies, tell jokes, or just chat with you.")
        elif user_input == "tell me a joke":
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif user_input == "recommend a movie":
            print("Chatbot: What genre are you in the mood for? (e.g., Action, Comedy, Drama)")
            genre_input = input().lower()
            recommend_movie(genre_input)
        elif user_input == "provide information":
            provide_information()
        elif user_input == "what is your purpose?":
            print("Chatbot: My purpose is to assist and provide information to the best of my abilities.")
        elif user_input == "who created you?":
            print("Chatbot: I was created by a team of developers for learning and demonstration purposes.")
        elif user_input == "how do you work?":
            print("Chatbot: I use a rule-based approach to respond to specific inputs. For more advanced functionality, machine learning-based chatbots are employed.")
        elif user_input == "feedback":
            print("Chatbot: How would you rate your interaction with me? (1-5)")
            rating = int(input())
            process_feedback(rating)
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. If you have a specific question, feel free to ask!")

if __name__ == "__main__":
    main()


