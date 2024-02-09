from flask import Flask, request, jsonify
import requests
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_gmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_gmail_password'

mail = Mail(app)

def send_notification(sum_result):
    if sum_result > 50:
        url = "https://example.com/notify" 
        payload = {'sum': sum_result}
        requests.post(url, json=payload)

@app.route('/sum', methods=['GET'])
def sum_numbers():
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 + num2
        send_notification(result)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide valid integer values for num1 and num2.'}), 400
        
@app.route('/notify', methods=['POST'])
def send_email_notification():
    try:
        recipient = request.form.get('recipient')
        subject = request.form.get('subject')
        body = request.form.get('body')

        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
        msg.body = body

        mail.send(msg)

        return jsonify({'message': 'Email notification sent successfully.'})
    except Exception as e:
        return jsonify({'error': 'Failed to send email notification.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run()
