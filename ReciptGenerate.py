from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Function to generate receipt PDF
def generate_receipt(user_name, email, product_name, collection_date, condition, usage, reward_points):
    # Ensure file name is valid (no spaces or special characters)
    receipt_filename = f"{user_name.replace(' ', '_')}_receipt.pdf"
    
    # Define where to save the file
    output_folder = "receipts"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the folder if it doesn’t exist

    full_path = os.path.join(output_folder, receipt_filename)

    try:
        c = canvas.Canvas(full_path, pagesize=letter)
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

        # Footer
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(50, 540, "Thank you for recycling responsibly! 🌍💚")
        c.drawString(50, 520, "Visit GreenTalk for more details: www.greentalk.com")

        # Save and close the PDF
        c.save()
        print(f"Receipt successfully generated: {full_path}")
        return full_path

    except Exception as e:
        print(f"Error generating receipt: {e}")
        return None


receipt_path = generate_receipt(
    user_name="John Doe",
    email="johndoe@gmail.com",
    product_name="Laptop - Dell XPS 13",
    collection_date="2025-02-15",
    condition="Good",
    usage=3,
    reward_points=50
)

if receipt_path:
    print(f"📄 Receipt generated successfully at: {receipt_path}")
else:
    print("Failed to generate receipt.")


###Recipt send to the mail 

