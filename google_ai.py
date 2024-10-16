# Import the Python SDK
import google.generativeai as genai

import hidden


GOOGLE_API_KEY = hidden.google_ai_api_key()


genai.configure(api_key=GOOGLE_API_KEY)


file_path = "receipt_image\IMG_0787.png"
myfile = genai.upload_file(file_path)
print(f"{myfile=}")

model = genai.GenerativeModel("gemini-1.5-flash")

result = model.generate_content(
    [
        myfile, "\n\n",
        """
        Analyze the receipt text below and convert it into a structured JSON object. The JSON should have the following fields:

        - "store_name": Name of the store.
        - "address": An object containing:
        - "street": The street address.
        - "city": The city.
        - "state": The state.
        - "zip": The ZIP code.
        - "date": The purchase date in the format "YYYY-MM-DD".
        - "time": The purchase time in the format "HH:MM:SS".
        - "items": An array of objects where each item contains:
        - "name_on_receipt": The name as it appears on the receipt.
        - "name": The name of the item.
        - "category": The category of the item 
                (Available categories:
                "Food & Beverage",
                "Health & Beauty",
                "Household Essentials",
                "Home Goods",
                "Electronics",
                "Baby, Kids & Pets",
                "Clothing & Accessories",
                "Automotive",
                "Sports & Outdoors",
                "Pharmacy").
        - "quantity": The number of units purchased.
        - "unit_price": The price per unit.
        - "total_price": The total price for the item (calculated as quantity * unit_price).
        - "subtotal": The subtotal amount before tax.
        - "tax": The tax amount.
        - "grand_total": The final total including tax.
        - "payment_method": An object containing:
        - "type": The type of payment (e.g., "Credit Card", "Cash").
        - "provider": The payment provider (e.g., "Visa").
        - "last_four_digits": The last four digits of the card used, if applicable. (Keep it to four digits if it's longer)
        - "discount": Any discount applied (use 0.0 if none).
        - "tip": Any tip amount (use 0.0 if none).

        If any information is missing or not available, use "null" as the value.
        """
    ],
    generation_config = {"temperature": 0.0}
)

with open(r"output\googleAI.txt", "w") as f:
    f.write(result.text)


# Parse the store name, the purchased items, the price of the items, and the category for items. Return a JSON object.
# Here's the JSON example:
# {
#     "receipt": {
#         "store_name": "Grocery Mart",
#         "address": {
#             "street": "123 Main St",
#             "city": "City",
#             "state": "State",
#             "zip": "ZIP"
#         },
#         "date": "2024-10-16",
#         "time": "14:30:00",
#         "items": [
#             {
#                 "name": "Bananas",
#                 "category": "Food & Beverage",
#                 "quantity": 1,
#                 "unit_price": 0.59,
#                 "total_price": 0.59
#             },
#         ],
        
#         "subtotal": 36.80,
#         "tax": 2.21,
#         "grand_total": 39.01,
#         "payment_method": {
#             "type": "Credit Card",
#             "provider": "Visa",
#             "last_four_digits": "1234"
#         },
#         "discount": 0.0,
#         "tip": 0.0
#     }
# }