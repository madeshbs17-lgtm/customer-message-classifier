# Customer Message Classifier

An LLM-powered customer support message classification project built with Python, Google's Gemini API, Pydantic, and Streamlit.

The application is designed to classify customer messages into four categories:
- Complaint
- Refund Request
- Product Question
- General Inquiry

## Features

- **LLM-based classification:** Uses Google's Gemini API to classify customer messages.
- **Prompt Engineering:** Uses explicit instructions and classification rules to guide predictions.
- **Structured Output:** Requests JSON responses from the model.
- **Data Validation:** Uses Pydantic to validate classification results.
- **Interactive Interface:** Provides a Streamlit web interface.
- **Demo Mode:** Includes predefined examples to demonstrate the interface without API requests.

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- Pydantic
- Streamlit
- Pandas
- python-dotenv

## Project Structure

```text
customer-message-classifier/
├── data/
│   └── test_messages.csv
├── app.py
├── evaluate.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

The `.env` file contains your API key and must not be uploaded to GitHub.

## Setup Instructions

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd customer-message-classifier
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key. Never commit this file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local address displayed in your terminal.

## Demo Mode

The application currently supports a demo mode with predefined examples.

For example:

**Input:**
"My order arrived damaged. I am very disappointed."

**Output:**
Complaint

Demo mode only recognizes predefined messages. Actual AI classification requires a working Gemini API connection and available API quota.

## Evaluation

The project includes an evaluation script and a CSV dataset containing labeled test messages.

A complete evaluation has not yet been verified. Accuracy results will be added after the evaluation runs successfully.

## Future Improvements

- Complete model evaluation and report classification accuracy.
- Analyze misclassified examples.
- Improve classification robustness.
- Add support for more customer message categories.
- Deploy the application for public access.

## Learning Outcomes

This project provides practical experience with:

- LLM API integration
- Prompt engineering
- JSON parsing
- Pydantic validation
- Building interactive applications with Streamlit
- Organizing a Python project
- Evaluating a text classification system