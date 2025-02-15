import spacy
import random

# Load NLP Model
nlp = spacy.load("en_core_web_sm")

# Predefined chatbot responses
responses = {
    "greeting": [
        "Hello! Welcome to ECoWaste. How can I assist you today?",
        "Hi there! Let’s talk about responsible e-waste recycling. How can I help?",
        "Hey!   Got questions about e-waste? I'm here to help!"
    ],
    "who_are_you": [
        "I’m GreenTalk AI, your assistant for e-waste recycling! ",
        "I help individuals, businesses, and retailers recycle their e-waste responsibly.",
        "I'm an AI built to guide you on e-waste management!"
    ],
    "what_is_ewaste": [
        "E-Waste includes old phones, laptops, chargers, TVs, and batteries.",
        "Electronic waste refers to discarded devices that should be disposed of properly.",
        "E-waste is any outdated or broken electronic device that needs proper recycling."
    ],
    "why_use_platform": [
        "Free doorstep pickup \n Eco-friendly disposal \n Instant cashback \n Secure data wiping ",
        "You should use ECoWaste for **safe, legal, and rewarding e-waste disposal!**",
        "Our platform offers **free pickup, cashback, and responsible recycling**."
    ],
    "pickup": [
        "We offer **free doorstep pickup** in most locations. Schedule a pickup on our website!",
        "You can also drop off your e-waste at our nearest collection center.",
        "To schedule a pickup, visit your dashboard and select a date!"
    ],
    "rewards": [
        "Earn cashback, discount coupons, and exclusive rewards when you recycle with us! ",
        "By recycling, you get **instant cashback** and **discounts on future purchases**.",
        "Your responsible actions help the planet, and we reward you for it!"
    ],
    "individual": [
        "As an individual, you can recycle your old phone, laptop, or gadgets and get rewards!",
        "Individuals can **schedule pickups** and receive cashback instantly!",
        "Recycling is easy! Just book a pickup and get rewarded."
    ],
    "retailer": [
        "Retailers can recycle unsold or defective electronics in bulk and **earn incentives**.",
        "We offer **bulk e-waste disposal programs** with added benefits for retailers.",
        "Businesses & retailers can dispose of their electronic waste in bulk and receive rewards."
    ],
    "business": [
        "Businesses can request bulk pickup for office electronics and receive **compliance certificates.**",
        "We provide **secure e-waste disposal** and **data destruction** for businesses.",
        "Your company can safely dispose of old computers, printers, and other office electronics."
    ],
    "dispose": [
        "Yes! You can dispose of old smartphones, laptops, and electronic waste through our **free pickup service.**",
        "We help you dispose of old electronics **safely and legally** while earning cashback!",
        "Disposing of e-waste responsibly prevents pollution and supports sustainability!"
    ],
    "bulk_waste": [
        "For **bulk waste disposal**, businesses and retailers can schedule a **special pickup**.",
        "We offer **bulk recycling programs** with cashback for large e-waste collections.",
        "To dispose of a large amount of e-waste, contact our support for a custom pickup!"
    ],
    "unknown": [
        "I'm still learning! 🌱 Please check our FAQs or visit our website for more info.",
        "That’s an interesting question! Let me find an answer for you.",
        "I'm not sure about that, but I can help with e-waste-related questions!"
    ]
}

## Function to process user input using NLP
def classify_intent(user_input):
    user_input = user_input.lower()
    doc = nlp(user_input)

    # Keyword-based matching with NLP tokenization
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey", "greetings","hii","Hii","hiii","helloo"]:
            return "greeting"
        elif token.lemma_ in ["who", "what", "you","why"]:
            return "who_are_you"
        elif token.lemma_ in ["ewaste", "e-waste", "electronic waste", "scrap",]:
            return "what_is_ewaste"
        elif "why" in user_input and "use" in user_input:
            return "why_use_platform"
        elif "pickup" in user_input or "collect" in user_input:
            return "pickup"
        elif "reward" in user_input or "cashback" in user_input:
            return "rewards"
        elif "individual" in user_input:
            return "individual"
        elif "retailer" in user_input or "shop" in user_input:
            return "retailer"
        elif "business" in user_input or "corporate" in user_input:
            return "business"
        elif "dispose" in user_input or "throw away" in user_input:
            return "dispose"
        elif "bulk" in user_input or "large amount" in user_input:
            return "bulk_waste"

    return "unknown"  # If no category matches, return "unknown"

# Simple chatbot loop for testing
if __name__ == "__main__":
    print("🌱 GreenTalk AI - E-Waste Chatbot (Type 'exit' to end)")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("GreenTalk: Thank you for chatting! Let's keep our planet green! 🌍💚")
            break

        # Get classified intent and response
        intent = classify_intent(user_input)
        response = random.choice(responses[intent])
        print(f"GreenTalk: {response}")

