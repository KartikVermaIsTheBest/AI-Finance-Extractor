# AI Finance Extractor

An AI-powered finance extraction tool built using Python, Google Gemini API, and Pandas.

## Overview

This project takes financial statements written in natural language and automatically extracts structured financial transactions using Google's Gemini AI model.

The extracted data is converted into JSON, analyzed to calculate income, expenses, and savings, and then exported to a CSV file for further processing.

## Features

* Natural language financial statement processing
* AI-powered transaction extraction using Gemini API
* Structured JSON output
* Income and expense calculation
* Savings calculation
* CSV export using Pandas
* Error handling for API failures

## Example

### Input

```text
I bought flowers for 5000 rupees and earned 10000 rupees from mechanics work.
```

### Extracted Transactions

```json
[
  {
    "type": "expense",
    "description": "flowers",
    "amount": 5000,
    "currency": "rupees"
  },
  {
    "type": "income",
    "description": "mechanics work",
    "amount": 10000,
    "currency": "rupees"
  }
]
```

### Output

```text
Income = 10000
Expense = 5000
Savings = 5000
```

## Tech Stack

* Python
* Google Gemini API
* Pandas
* JSON

## Installation

1. Clone the repository

```bash
git clone https://github.com/KartikVermaIsTheBest/AI-Finance-Extractor.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a file named `secret_key.py`

```python
gemini_key = "YOUR_API_KEY"
```

4. Run the project

```bash
python main.py
```

## Project Workflow

```text
User Input
     ↓
Gemini API
     ↓
JSON Response
     ↓
Python Processing
     ↓
Income / Expense Analysis
     ↓
Pandas DataFrame
     ↓
CSV Export
```

## Future Improvements

* Expense categorization
* Data visualizations and charts
* Flask web application
* PDF bank statement processing
* Interactive dashboard

## Author

Kartik Verma
