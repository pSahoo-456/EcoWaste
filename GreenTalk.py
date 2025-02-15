import random

class GreenTalkAI:
    def __init__(self):
        self.responses = {
            "greeting": ["Hi! 🌱 Ready to make a difference? Ask me anything about e-waste recycling!", 
                         "Hello! 🌍 Let’s work together for a cleaner planet. How can I help?"],
            
            "what is e-waste": ["E-waste refers to discarded electronic devices like phones, laptops, and appliances. They contain hazardous materials but can be recycled to reduce pollution. 🌱♻️",
                                "E-waste, or electronic waste, includes old gadgets like smartphones, computers, and TVs that need proper disposal or recycling to prevent environmental damage."],
            
            "why use your platform": ["GreenTalk helps you recycle electronic waste responsibly, earn rewards, and contribute to a sustainable future! 🌍💚",
                                      "Our platform makes e-waste recycling **easy, rewarding, and eco-friendly**. Join us in reducing pollution! ♻️"],
            
            "how your platform helps me": ["We offer **free e-waste collection, instant valuation, and rewards** for recycling your gadgets. Let’s make a greener future together! 🌱",
                                           "By using our platform, you can **dispose of old devices, earn rewards, and help the planet**. Win-win! 🌎"],
            
            "rewards": ["By recycling, you **earn discounts, cashback, or even donations to environmental causes**. It’s our way of thanking you! 🎁",
                        "Recycle with us and get **vouchers, discounts, or even plant a tree in your name**! 🌳💚"],
            
            "login page": ["You can access the login page by clicking on the 'Login' button at the top of our website. Let me know if you need help!"],
            
            "examples of e-waste": ["Examples of e-waste include **smartphones, laptops, tablets, TVs, printers, chargers, and batteries**. Do you have something to recycle?"],
            
            "eco-waste": ["Eco-waste generally refers to biodegradable waste from organic materials, while **e-waste specifically refers to electronic waste like phones and computers**. ♻️"],
            
            "e-waste recycling": ["E-waste recycling helps recover valuable materials like **gold, silver, and copper** while preventing harmful chemicals from polluting the environment. 🌍"],
            
            "how much money will I get": ["The price depends on your device's condition, brand, and market value. You can check our valuation tool on the website for an estimate! 📱💰"],
            
            "dispose of old device": ["Great! You can **schedule a free pickup** or drop it at a nearby collection center. Let’s recycle responsibly! 🌱"],
            
            "where is the nearest recycling center": ["You can find the nearest e-waste recycling center on our website’s ‘Find a Center’ section. Type your city name, and we’ll guide you! 🌍"],
            
            "why is e-waste harmful": ["E-waste contains **lead, mercury, and other toxic substances** that can pollute soil and water if not disposed of properly. That’s why recycling is crucial!"],
            
            "default": ["That’s an interesting question! Let me find an answer for you. Meanwhile, check out our website for more details. 🌱",
                        "I’m still learning! But you can explore our FAQs for a detailed answer. Let’s keep our planet green! 🌍💚"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses.keys():
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])


# Run the chatbot
if __name__ == "__main__":
    bot = GreenTalkAI()
    print("🌱 GreenTalk AI - E-Waste Chatbot (Type 'exit' to end)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("GreenTalk: Thanks for chatting! Keep recycling and making a difference. ♻️🌍")
            break
        response = bot.get_response(user_input)
        print(f"GreenTalk: {response}")


