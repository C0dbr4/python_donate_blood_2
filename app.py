from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' and 'YOUR_TELEGRAM_GROUP_ID' with your actual bot token and group ID
TELEGRAM_BOT_TOKEN = '6691298966:AAG4XGVf2aPw47HBUxTLUSmxjPgLJPBkM7U'
TELEGRAM_GROUP_ID = '-4188089568'

def send_to_telegram(data):
    message = f"New registration:\nName: {data['name']}\nPhone: {data['phone']}\nLocation: {data['location']}\nBlood Group: {data['blood_group']}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_GROUP_ID}&text={message}"
    requests.get(url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = {
        'name': request.form['name'],
        'phone': request.form['phone'],
        'location': request.form['location'],
        'blood_group': request.form['blood_group']
    }
    send_to_telegram(data)
    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True)
