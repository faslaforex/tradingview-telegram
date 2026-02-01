from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8356334314:AAF0R8Y1Vi7IOiCEIy8trmGFJnzbOb8RZlE"
TELEGRAM_CHAT_ID = "7242939346"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        if data:
            message = f"تنبيه من TradingView:\n\n{data}"
        else:
            message = "تنبيه من TradingView"
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        response = requests.post(telegram_url, json=payload)
        return {"status": "success"}, 200
    except Exception as e:
        print(f"Error: {e}")
        return {"status": "error"}, 500

@app.route('/')
def home():
    return "Bot is running"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
