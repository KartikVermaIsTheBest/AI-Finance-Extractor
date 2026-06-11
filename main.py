import json
import pandas as pd

from google import genai
from secret_key import gemini_key

client = genai.Client(api_key=gemini_key)

text = input("Enter Financial Statement: ")
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Extract financial transactions.

        Return ONLY valid JSON.

        Format:

        [
            {{
                "type": "income",
                "description": "",
                "amount": 0,
                "currency": "rupees"
            }}
        ]

        Rules:
        1. type must be either "income" or "expense"
        2. amount must be numeric
        3. return only JSON
        4. do not add explanations
        5. turn everything to Capital

        Text:
        {text}
        """
    )

    response_text = response.text.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "", 1)

    if response_text.endswith("```"):
        response_text = response_text[:-3]

    response_text = response_text.strip()

    data = json.loads(response_text)

    print(data)

    total_income = 0
    total_expense = 0

    for transaction in data:
        transaction_type = transaction.get("type")
        amount = transaction.get("amount", 0)

        if transaction_type == "income":
            total_income += amount

        elif transaction_type == "expense":
            total_expense += amount
    savings = total_income - total_expense

    print("Income =", total_income)
    print("Expense =", total_expense)
    print("Savings =", savings)

    df = pd.DataFrame(data)

    print(df)

    df.to_csv("transactions.csv", index=False)

    print("CSV saved successfully!")


except Exception as e:
    print("Error:", e)
