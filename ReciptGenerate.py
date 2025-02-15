
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib
import os

# Function to generate receipt PDF
def generate_receipt(user_name, email, product_name, collection_date, condition, usage, reward_points):
    receipt_filename = f"{user_name}_receipt.pdf"
    
    c = canvas.Canvas(receipt_filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    
    # Title
    c.drawString(200, 750, "🌱 GreenTalk - E-Waste Collection Receipt ♻️")
    
    # User Information
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"User Name: {user_name}")
    c.drawString(50, 680, f"Email: {email}")
    c.drawString(50, 660, f"Product Name: {product_name}")
    c.drawString(50, 640, f"Collection Date: {collection_date}")
    c.drawString(50, 620, f"Condition: {condition}")
    c.drawString(50, 600, f"Usage Duration: {usage} years")
    c.drawString(50, 580, f"Earned Reward Points: {reward_points}")
    c.drawAlignedString(50)

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 540, "Thank you for recycling responsibly! 🌍💚")
    c.drawString(50, 520, "Visit GreenTalk for more details: www.greentalk.com")

    c.save()
    print(f"Receipt generated: {receipt_filename}")
    
    return receipt_filename
