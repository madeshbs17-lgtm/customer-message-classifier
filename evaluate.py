import os
import json
import time
import pandas as pd

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
from typing import Literal


# 1. Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


# 2. Define the expected response
class ClassificationResult(BaseModel):
    category: Literal[
        "complaint",
        "refund_request",
        "product_question",
        "general_inquiry"
    ]


# 3. Define the classification prompt
def classify_message(message):
    prompt = f"""
    You are a customer support message classifier.

    Classify the message into exactly one category:
    - complaint
    - refund_request
    - product_question
    - general_inquiry

    Rules:
    1. Explicit refund requests take priority.
    2. Otherwise, complaints about problems or dissatisfaction are complaint.
    3. Questions about product features are product_question.
    4. Other general questions are general_inquiry.

    Return JSON only:
    {{"category": "one permitted category"}}

    Customer message: {message}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config={"http_options": {"timeout": 30000}}
    )

    result = json.loads(response.text)

    validated_result = ClassificationResult.model_validate(result)

    return validated_result.category


# 4. Load the dataset
df = pd.read_csv("data/test_messages.csv")

print(f"Total messages: {len(df)}")
print("Evaluating classifier...\n")


# 5. Classify each message
predictions = []

for index, row in df.iterrows():
    try:
        prediction = classify_message(row["message"])
        predictions.append(prediction)

        print(f"{index + 1}/{len(df)}: {prediction}")

    except Exception as error:
        print(f"{index + 1}/{len(df)}: Error - {error}")
        predictions.append("ERROR")

    # Avoid sending requests too rapidly.
    if index < len(df) - 1:
        time.sleep(15)


# 6. Compare predictions with actual categories
df["predicted_category"] = predictions
df["correct"] = (
    (df["category"] == df["predicted_category"])
    & (df["predicted_category"] != "ERROR")
)

correct_predictions = df["correct"].sum()
total_messages = (df["predicted_category"] != "ERROR").sum()

if total_messages == 0:
    print("No messages were classified successfully. Try again later.")
    raise SystemExit(1)

accuracy = (correct_predictions / total_messages) * 100

print("\n--- Evaluation Results ---")
print(f"Correct predictions: {correct_predictions}/{total_messages}")
print(f"Accuracy: {accuracy:.2f}%")


# 7. Save detailed results
df.to_csv("evaluation_results.csv", index=False)

print("\nDetailed results saved to evaluation_results.csv")