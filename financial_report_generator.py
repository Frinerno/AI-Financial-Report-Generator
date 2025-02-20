import pandas as pd
import openai
import os
from dotenv import load_dotenv

# Load OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_financial_report(csv_file):
    df = pd.read_csv(csv_file)
    stats = df.describe().to_string()
    prompt = f"Based on the following financial statistics, generate a detailed report highlighting trends and insights:\n{stats}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial analyst."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    csv_file = input("Enter path to the financial CSV file: ")
    report = generate_financial_report(csv_file)
    print("\nFinancial Report:\n", report)
