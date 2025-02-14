import random
import json
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load Pretrained Transformer Model (Optional, for advanced responses)
model_name = "facebook/blenderbot-400M-distill"  # Conversational AI model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Load predefined responses
responses = {
    "greeting": [
        "Hello! I'm GreenTalk, your eco-friendly assistant. 🌱 How can I help you?",
        "Hey there! I'm GreenTalk, here to guide you in recycling e-waste. How can I assist you today?",
        "Hi! 🌍 Let's make the planet greener together. Ask me anything about e-waste!"
    ],
    "recycle_importance": [
        "Did you know? **80% of e-waste is not recycled properly**, causing pollution! Let's change that! 🌿♻️",
        "Recycling e-waste saves natural resources and **reduces toxic waste**. Join the movement! 🌎",
        "By recycling old electronics, we can **prevent hazardous materials from polluting soil and water**. 🌱💡"
    ],
    "how_to_dispose": [
        "To dispose of e-waste: 1️⃣ Find a certified recycling center. 2️⃣ Drop off your old electronics. 3️⃣ Get rewards for responsible disposal! ♻️",
        "Not sure where to dispose of e-waste? Use our **locator tool** to find nearby recycling stations. 📍",
        "Dispose of e-waste **safely and legally**. Avoid throwing electronics in regular trash! 🚫🗑️"
    ],
    "rewards": [
        "Great news! By recycling, you can **earn discounts & rewards** for your next gadget purchase! 🎁💰",
        "Every time you recycle, you **get GreenPoints**, which can be redeemed for eco-friendly products. 🌿💚"
    ],
    "environmental_impact": [
        "E-waste contains **lead, mercury, and arsenic**. If not recycled, they contaminate the air, water, and soil. 🚨",
        "A single discarded phone **pollutes 40,000 liters of water**. Imagine the impact of millions of devices! 🚱",
        "Proper recycling can **reduce CO₂ emissions by 50%**. Let's act responsibly! 🌎💙"
    ],
    "e_products_disposal": [
        "Different e-products need different disposal methods. 📱 Laptops, phones, and batteries should go to **certified recyclers**.",
        "For large appliances like **TVs, refrigerators, and washing machines**, schedule a pickup with an e-waste facility. 🚛♻️"
    ],
    "user_guidance": [
        "Our platform helps you: 1️⃣ Check your device’s expiry 2️⃣ Find the best recycling options 3️⃣ Get rewards! 🌍💚",
        "Want to recycle? **Upload your device details**, and we’ll guide you through safe disposal! 🚀"
    ],
    "default": [
        "I'm still learning! 🤖 But I can definitely help with e-waste and recycling. Try asking me something else!",
        "Hmmm... I don’t have an answer for that, but let's talk about recycling! ♻️",
    ]
}

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()

    # Intent Matching
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"])
    elif any(word in user_input for word in ["why recycle", "importance of recycling", "why should i recycle"]):
        return random.choice(responses["recycle_importance"])
    elif any(word in user_input for word in ["how to dispose", "where to dispose", "throw away electronics"]):
        return random.choice(responses["how_to_dispose"])
    elif any(word in user_input for word in ["rewards", "benefits", "incentives", "what do i get"]):
        return random.choice(responses["rewards"])
    elif any(word in user_input for word in ["environment", "pollution", "impact"]):
        return random.choice(responses["environmental_impact"])
    elif any(word in user_input for word in ["dispose old tv", "throw old laptop", "phone disposal"]):
        return random.choice(responses["e_products_disposal"])
    elif any(word in user_input for word in ["how to use", "guide me", "platform help"]):
        return random.choice(responses["user_guidance"])
    
    # Use AI Model for unknown questions
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(input_ids, max_length=50)
    ai_response = tokenizer.decode(output[0], skip_special_tokens=True)

    return ai_response if ai_response else random.choice(responses["default"])

# Chat Loop
print("🌱 GreenTalk AI - E-Waste Chatbot (Type 'exit' to end)")
while True:
    user_query = input("You: ")
    if user_query.lower() == "exit":
        print("GreenTalk: Thank you for being eco-friendly! ♻️🌍 See you again!")
        break
    print("GreenTalk:", get_response(user_query))
