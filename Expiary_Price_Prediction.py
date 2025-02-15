import random

# Predefined chatbot responses
responses = {
    "greeting": [
        "Hello! 🌱 Welcome to GreenTalk AI. How can I assist you today?",
        "Hi there! 🌍 Let’s talk about responsible e-waste recycling. How can I help?"
    ],
    "who_are_you": [
        "I’m GreenTalk AI, your assistant for e-waste recycling! ♻️",
        "I help individuals, businesses, and retailers recycle their e-waste responsibly."
    ],
    "what_is_ewaste": [
        "E-Waste includes old phones, laptops, chargers, TVs, and batteries.",
        "Electronic waste refers to discarded devices that should be disposed of properly."
    ],
    "why_use_platform": [
        "✅ Free doorstep pickup 🚚 \n✅ Eco-friendly disposal ♻️ \n✅ Earn rewards 💰 \n✅ Secure data wiping 🔒",
        "Use our platform for **safe, legal, and rewarding e-waste disposal.**"
    ],
    "pickup": [
        "We offer **free doorstep pickup** in most locations. Schedule a pickup on our website!",
        "You can also drop off your e-waste at our nearest collection center."
    ],
    "rewards": [
        "Earn cashback, discount coupons, and reward points when you recycle with us! 🎟️💰",
        "By recycling, you get **discounts, cashback, and redeemable points.**"
    ],
    "individual": [
        "As an individual, you can recycle your old phone, laptop, or gadgets and get rewards!",
        "Individuals can **schedule pickups** and get incentives for responsible e-waste disposal."
    ],
    "retailer": [
        "Retailers can recycle unsold or defective electronics in bulk and **earn incentives**.",
        "We offer **bulk e-waste disposal programs** for retailers with added benefits."
    ],
    "business": [
        "Businesses can request bulk pickup for office electronics and receive **compliance certificates.**",
        "We provide **secure e-waste disposal** and **data destruction** for businesses."
    ],
    "dispose": [
        "Yes! You can dispose of old smartphones, laptops, and electronic waste through our **free pickup service.**",
        "We help you dispose of old electronics **safely and legally** while earning rewards."
    ],
    "bulk_waste": [
        "For **bulk waste disposal**, businesses and retailers can schedule a **special pickup**.",
        "We offer **bulk recycling programs** with rewards for large e-waste collections."
    ],
    "default": [
        "I'm still learning! 🌱 Please check our FAQs or visit our website for more info.",
        "That’s an interesting question! Let me find an answer for you."
    ]
}

#

