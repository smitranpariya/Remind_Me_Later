from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(8), nullable=False)
    message = db.Column(db.Text, nullable=False)
    reminder_type = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create DB tables
with app.app_context():
    db.create_all()

# API endpoint to create a reminder
@app.route('/api/reminders', methods=['POST'])
def create_reminder():
    data = request.get_json()

    required_fields = ['date', 'time', 'message', 'reminder_type']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f"'{field}' is required"}), 400

    new_reminder = Reminder(
        date=data['date'],
        time=data['time'],
        message=data['message'],
        reminder_type=data['reminder_type']
    )

    db.session.add(new_reminder)
    db.session.commit()

    return jsonify({
        'id': new_reminder.id,
        'date': new_reminder.date,
        'time': new_reminder.time,
        'message': new_reminder.message,
        'reminder_type': new_reminder.reminder_type,
        'created_at': new_reminder.created_at.isoformat()
    }), 201

# Simple health check
@app.route('/')
def index():
    return 'Remind-me-later API is running!'

if __name__ == '__main__':
    app.run(debug=True)
