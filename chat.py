1.) chatbot

import re
responses= {
    "hello":"Hello! How can I assist you today?",
    "price": "Can you please specify whch product or servce you are asking for?",
    "information": "Our company name is ABC enterprices and we are in the business of electronics equipment",
    "name": "Our company is ABC Enterprices PVT LTD",
    "hours": "Our business hours are Monday to Friday, 9AM to 5PM",
    "address":"We are located at 134 Main Street,Springfield",
    "contact": "You can reach us at contact@example.com or call us at (455)1234688.",
    "help":"I am here to help you.Please ask me anything",
    "default": "I am sorry,I didn't understand that.Can you please provide me some more details?"
}

def get_response(message):
    message=message.lower()

    for key in responses:
        if re.search(r'\b' + re.escape(key) + r'\b',message):
            return responses[key]

    return responses["default"]

def chatbot():

    print("Welcome to our customer service chatbot! Ask me anything about the organization.Type 'exit' to end the chat ")

    while True:
        user_input= input("You: ")
        if user_input.lower()== 'exit':
          print("ChatBot: Goodbye! Have a great day!")
          break
        response=get_response(user_input)
        print(f"Chatbot:{response}")
if __name__== "__main__":
        chatbot()
