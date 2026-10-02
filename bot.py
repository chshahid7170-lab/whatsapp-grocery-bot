# M Shahid Fareed - WhatsApp Grocery Bot
# This bot reads prices from Google Sheets

def get_price(product_name):
    # Sample data - in real project this connects to Google Sheets API
    products = {
        "soap": "Price: 180 Rs",
        "oil": "Price: 450 Rs",
        "sugar": "Price: 165 Rs / KG"
    }
    return products.get(product_name.lower(), "Sorry, product not found in list.")

# Test the bot
user_message = input("Customer ne kya pucha? : ")
print(get_price(user_message))
