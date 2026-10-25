# Customer Message Classifier

An LLM-powered customer support message classification project built with Python, Google's Gemini API, Pydantic, and Streamlit.

The application classifies customer messages into four categories:

- **Complaint** — Messages expressing dissatisfaction with a product or service.
- **Refund Request** — Messages requesting a refund or return of payment.
- **Product Question** — Messages asking questions about a product's features or specifications.
- **General Inquiry** — General customer questions that do not fit the other categories.

## Features

- **LLM-Based Classification:** Uses Google's Gemini API to classify customer messages.
- **Prompt Engineering:** Uses explicit instructions and classification rules to guide predictions.
- **Structured Output:** Requests structured JSON responses from the model.
- **Data Validation:** Uses Pydantic to validate classification results.
- **Interactive Interface:** Provides a web interface built with Streamlit.
- **Automated Evaluation:** Evaluates predictions against labeled test messages.
- **Error Handling:** Displays errors when classification requests fail.

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

**Note:** The `.env` file stores your Gemini API key locally. It should never be committed to GitHub. The `.gitignore` file excludes sensitive configuration and virtual environment files.

## Setup Instructions

### 1. Clone the Repository

Replace the placeholder below with your actual GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd customer-message-classifier
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your Gemini API Key

Create a `.env` file in the project root directory:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## Example Classification

**Input:**

```text
My order arrived damaged. I am very disappointed.
```

**Expected category:**

```text
Complaint
```

**Input:**

```text
I am not satisfied with the product quality. I want a refund.
```

**Expected category:**

```text
Refund Request
```

The application uses the Gemini API to generate classifications. Results depend on the model's response and the quality of the classification instructions.

## Evaluation

The project includes an evaluation script (`evaluate.py`) and a labeled test dataset (`data/test_messages.csv`) containing 10 customer messages.

### Preliminary Results

| Metric | Result |
|---|---:|
| Total test messages | 10 |
| Successful predictions | 8 |
| Failed API requests or responses | 2 |
| Correct predictions among successful requests | 8 |
| Preliminary accuracy on successful predictions | 100% |

**Important:** The 100% accuracy applies only to the eight successfully evaluated messages. Two messages could not be evaluated because of API response errors, so this result does not establish 100% accuracy across the complete dataset. The sample is also too small to establish general model performance.

To run the evaluation:

```bash
python evaluate.py
```

API quota limits, timeouts, and malformed responses may affect evaluation. Failed requests should be reported separately rather than counted as incorrect model predictions.

## Future Improvements

- Improve handling of API timeouts, quota limits, and malformed responses.
- Expand the labeled evaluation dataset.
- Analyze misclassified examples and improve classification prompts.
- Compare different prompts and model configurations.
- Add more customer support categories.
- Deploy the application for public access.

## Learning Outcomes

Through this project, I gained practical experience with:

- Integrating an LLM API into a Python application.
- Writing prompts for text classification.
- Working with structured JSON outputs.
- Validating model responses using Pydantic.
- Building interactive applications with Streamlit.
- Evaluating an LLM-powered classification system.
- Managing Python dependencies and environment variables.
- Using Git and GitHub for version control.