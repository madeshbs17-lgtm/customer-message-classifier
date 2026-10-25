import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
from typing import Literal

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found. Check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)


# Validate classification output
class ClassificationResult(BaseModel):
    category: Literal[
        "complaint",
        "refund_request",
        "product_question",
        "general_inquiry"
    ]


# Classify customer message
def classify_message(message):
    prompt = f"""
    You are a customer support message classifier.

    Classify the following customer message into exactly one category:

    - complaint
    - refund_request
    - product_question
    - general_inquiry

    Rules:
    1. If the customer explicitly requests a refund, choose refund_request,
       even if they also complain.
    2. If the customer expresses dissatisfaction without requesting a refund,
       choose complaint.
    3. If the customer asks about a product's features or specifications,
       choose product_question.
    4. For other general questions, choose general_inquiry.

    Return only valid JSON in this format:
    {{"category": "one permitted category"}}

    Customer message: {message}
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    result = json.loads(response.text)
    validated_result = ClassificationResult.model_validate(result)

    return validated_result.category


# Streamlit interface
st.set_page_config(
    page_title="Customer Message Classifier",
    page_icon="📩",
    layout="centered"
)

st.title("📩 Customer Message Classifier")

st.write(
    "Classify customer support messages into four categories "
    "using a Gemini-powered AI model."
)

st.info(
    "Categories: Complaint, Refund Request, "
    "Product Question, General Inquiry"
)

message = st.text_area(
    "Enter a customer message:",
    placeholder="Example: My order arrived damaged. I want a refund.",
    height=150
)

if st.button("Classify Message", type="primary"):
    if not message.strip():
        st.warning("Please enter a customer message.")
    else:
        try:
            with st.spinner("Analyzing your message with Gemini AI..."):
                category = classify_message(message)

            st.success("Classification completed!")
            st.subheader("Predicted Category")
            st.markdown(f"### {category.replace('_', ' ').title()}")

        except Exception as e:
            st.error(f"Classification failed: {e}")
