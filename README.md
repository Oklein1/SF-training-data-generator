# Salesforce Random Data Generator

## Overview

This Python script generates random datasets specifically designed for practicing with Salesforce data. Currently, it creates datasets for users, accounts, and opportunities, enabling users to familiarize themselves with Salesforce-like structures and functionalities.

## Features

- **User Data Generation**:
  - Full name
  - Email address
  - Phone number
  - Billing address
  - Active status

- **Account Data Generation**:
  - Company name
  - Number of employees
  - Owner ID
  - Billing details

- **Opportunity Data Generation**:
  - Amount
  - IsWon and IsClosed status
  - Stage name
  - Associated account and owner IDs


## Setup Instructions

### For macOS / Windows

1. **Install Python**: Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

2. **Create a Virtual Environment**:
```bash
   python3 -m venv venv
```


3. **Activate Virtual Env** :
```bash
source venv/bin/activate
```

or on Windows:

```bash
venv\Scripts\activate
```

4. **Install Libraries**:
```bash
pip install -r requirements.txt
```

5. **Run Script**:
```bash
python3 main.py

```
