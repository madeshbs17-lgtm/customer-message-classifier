import os
import json
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
from google import genai


class ClassificationResult(BaseModel):
    category: Literal[
        "complaint",
        "refund_request",
        "product_question",
        "general_inquiry"
    ] = Field(description="The category assigned to the customer message")



# Load environment variables
load_dotenv()

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

# Create the Gemini client
client = genai.Client(api_key=api_key)

# Customer message to classify
customer_message = "My product arrived damaged, and I want my money back."

# Prompt for the LLM
prompt = f"""
You are a customer support message classifier.

Classify the customer message into exactly one of these categories:

1. complaint
2. refund_request
3. product_question
4. general_inquiry

Rules:
1. If the customer explicitly requests a refund, choose refund_request.
2. Otherwise, if the customer reports a problem or expresses dissatisfaction, choose complaint.
3. Otherwise, if the customer asks about product features or specifications, choose product_question.
4. Otherwise, choose general_inquiry.

Important:
- Select exactly one category.
- Follow the rules in order of priority.
- Do not invent information that is not present in the message.
- Return the result as a JSON object in this exact format:
 "category": "refund_request"

The category value must be one of:
complaint, refund_request, product_question, general_inquiry.

Return valid JSON only, without Markdown or explanations.

Customer message: {customer_message}
"""

# Send the prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={"http_options": {"timeout": 30000}}
)

# Display the result
print("Customer message:", customer_message)

result = json.loads(response.text)

validated_result = ClassificationResult.model_validate(result)

print("Predicted category:", validated_result.category)