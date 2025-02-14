import pandas as pd
import random

#  Expanded product categories with brands
product_brands = {
    "Laptop": ["Dell", "HP", "Lenovo", "Asus", "Apple", "Acer"],
    "Smartphone": ["Samsung", "Apple", "Xiaomi", "Realme", "OnePlus", "Vivo"],
    "TV": ["Samsung", "Sony", "LG", "TCL", "OnePlus"],
    "Refrigerator": ["LG", "Samsung", "Whirlpool", "Godrej", "Bosch"],
    "Washing Machine": ["Samsung", "LG", "Bosch", "Whirlpool", "IFB"],
    "Tablet": ["Apple", "Samsung", "Lenovo", "Huawei"],
    "Smartwatch": ["Apple", "Samsung", "Amazfit", "Boat", "Noise"],
    "Air Conditioner": ["Voltas", "LG", "Daikin", "Blue Star", "Carrier"],
    "Microwave": ["LG", "Samsung", "Panasonic", "IFB", "Morphy Richards"],
    "Gaming Console": ["Sony", "Microsoft", "Nintendo"],
    "DSLR Camera": ["Canon", "Nikon", "Sony", "Fujifilm"],
    "Electric Scooter": ["Ather", "Ola", "Hero", "TVS", "Bajaj"]
}

# Define realistic price ranges (in INR)
price_ranges = {
    "Laptop": (30000, 150000),
    "Smartphone": (8000, 120000),
    "TV": (15000, 200000),
    "Refrigerator": (20000, 80000),
    "Washing Machine": (15000, 60000),
    "Tablet": (10000, 80000),
    "Smartwatch": (3000, 50000),
    "Air Conditioner": (25000, 60000),
    "Microwave": (5000, 30000),
    "Gaming Console": (30000, 80000),
    "DSLR Camera": (40000, 200000),
    "Electric Scooter": (60000, 160000)
}

# Define build quality, usage, and condition
build_quality = [1, 2, 3, 4, 5]  # 1 = Poor, 5 = Excellent
usage_patterns = ["Light", "Moderate", "Heavy"]
conditions = [1, 2, 3, 4, 5]  # 1 = Worst, 5 = Best

# Generate complex dataset with 15,000 rows
data = []
for _ in range(15000):
    product_type = random.choice(list(product_brands.keys()))
    brand = random.choice(product_brands[product_type])
    build = random.choice(build_quality)
    usage = random.choice(usage_patterns)
    condition = random.choice(conditions)
    original_price = random.randint(*price_ranges[product_type])
    used_duration = random.randint(1, 12)

    # Assign user lifespan based on product type
    if product_type in ["Laptop", "Tablet", "Gaming Console"]:
        user_lifespan = round(random.uniform(3.5, 7.0), 1)
    elif product_type in ["Smartphone", "Smartwatch"]:
        user_lifespan = round(random.uniform(2.0, 5.0), 1)
    elif product_type in ["TV", "Refrigerator", "Washing Machine", "Air Conditioner"]:
        user_lifespan = round(random.uniform(8.0, 15.0), 1)
    elif product_type in ["Microwave", "DSLR Camera"]:
        user_lifespan = round(random.uniform(5.0, 10.0), 1)
    elif product_type == "Electric Scooter":
        user_lifespan = round(random.uniform(4.0, 8.0), 1)

    # Predict Expiry Years based on lifespan, quality, and usage
    expiry_years = user_lifespan + (0.2 * build) - (0.3 if usage == "Heavy" else 0.1 if usage == "Moderate" else 0)

    # Adjust depreciation factor dynamically based on category
    if product_type in ["Smartphone", "Smartwatch", "Tablet"]:
        depreciation_factor = (5 - condition) * 0.18  # Faster depreciation
    elif product_type in ["Gaming Console", "DSLR Camera"]:
        depreciation_factor = (5 - condition) * 0.12  # Slower depreciation
    else:
        depreciation_factor = (5 - condition) * 0.15  # Standard depreciation

    # Predict Current Price
    current_price = original_price * (1 - (used_duration / expiry_years)) * (1 - depreciation_factor)
    current_price = max(500, round(current_price, 2))  # Ensure min value

    data.append([product_type, brand, build, user_lifespan, usage, expiry_years, condition, original_price, used_duration, current_price])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Product_Type", "Brand", "Build_Quality", "User_Lifespan", "Usage_Pattern", 
    "Expiry_Years", "Condition", "Original_Price", "Used_Duration", "Current_Price"
])

# Save dataset
df.to_csv("expiry_price_data.csv", index=False)
print(" Dataset generated successfully and saved as 'expiry_price_data.csv'")
