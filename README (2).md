# IELTS Speaking Test Platform - Module 1 Assignment

## Overview

This assignment demonstrates basic Python scripting and Flask web development by building:
- A word counting utility (`word_counter.py`)
- A simple Flask API (`app.py`) with two routes

---

## Files

- `word_counter.py` — Standalone script to count words in a user-input string.
- `app.py` — Flask application with `/` and `/welcome` routes.
- `README.md` — This file, with instructions and test cases.

---

## Setup & Running Instructions

### Requirements

- Python 3.7+
- Flask (`pip install flask`)

### Running the Word Counter

```bash
python word_counter.py
```
- Enter any text at the prompt. The script displays the text and word count.
- Handles empty inputs and ignores extra spaces and punctuation.

### Running the Flask Application

```bash
export FLASK_APP=app.py
flask run
# OR
python app.py
```
- By default, the app runs on [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## API Endpoints & Test Cases

### `/` Route

- **Request:** `GET /`
- **Response:** Plain text — `Hello, Test Taker!`

#### Example

```bash
curl http://127.0.0.1:5000/
# Output: Hello, Test Taker!
```

---

### `/welcome` Route

- **Request:** `GET /welcome?name=<YourName>`
- **Response:** JSON: `{ "message": "Welcome to the IELTS Speaking Test, <YourName>!" }`

#### Examples

1. **Valid Name**
    ```bash
    curl "http://127.0.0.1:5000/welcome?name=John"
    ```
    **Response:**
    ```json
    {
      "message": "Welcome to the IELTS Speaking Test, John!"
    }
    ```

2. **Missing Name**
    ```bash
    curl "http://127.0.0.1:5000/welcome"
    ```
    **Response:**
    ```json
    {
      "error": "Missing 'name' query parameter."
    }
    ```
    *(HTTP 400 Bad Request)*

3. **Empty Name**
    ```bash
    curl "http://127.0.0.1:5000/welcome?name="
    ```
    **Response:**
    ```json
    {
      "error": "Name cannot be empty."
    }
    ```
    *(HTTP 400 Bad Request)*

---

## Notes

- The Flask code is thoroughly commented for clarity.
- Edge cases like missing or empty `name` parameters are handled gracefully.
- The word counter ignores special characters and whitespace when counting words.

---

## Author

Bharath-hub4
