# Remind-me-later API (Flask)

A simple REST API to accept reminders and store them in a SQLite database.

## Setup

1. Install dependencies:

pip install -r requirements.txt

2. Run the app:

python app.py

3. Test the API:

**POST** `http://127.0.0.1:5000/api/reminders`

**Body:**

```json
{
  "date": "YYYY-MM-DD",
  "time": "HH:MM:SS",
  "message": "Your reminder message",
  "reminder_type": "email/sms"
}