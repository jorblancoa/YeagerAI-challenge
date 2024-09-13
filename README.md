# YeagerAI-challenge

This repository contains solutions and tests for three coding challenges.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Code

To run a specific challenge, navigate to its directory and execute the Python file:

```bash
cd challenge_1
python challenge_1.py
```

## Running Tests

To run tests for a specific challenge:

```bash
pytest challenge_2/test_challenge_2.py
pytest challenge_3/test_challenge_3.py
```

To run all tests:

```bash
pytest
```