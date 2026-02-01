from flask import Flask, request
import requests
import os
import sys

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8356334314:AAF0R8Y1Vi7IOiCEIy8trmGFJnzbOb8RZlE"
TELEGRAM_CHAT_ID = "7242939346"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("=== WEBHOOK RECEIVED ===", file=sys.stderr, flush=True)
    try:
        data = request.get_json()
        print(f"Data: {data}", file=sys.stderr, flush=True)
        
        if data:
            message = str(data)
        else:
            message = "تنبيه من TradingView"
        
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
        
        print(f"Sending to Telegram...", file=sys.stderr, flush=True)
        response = requests.post(telegram_url, json=payload, timeout=10)
        print(f"Response: {response.status_code}", file=sys.stderr, flush=True)
        print(f"Response body: {response.text}", file=sys.stderr, flush=True)
        
        return {"status": "success"}, 200
        
    except Exception as e:
        print(f"=== ERROR: {str(e)} ===", file=sys.stderr, flush=True)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return {"status": "error", "message": str(e)}, 500

@app.route('/')
def home():
    return "Bot is running"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting on port {port}", file=sys.stderr, flush=True)
    app.run(host='0.0.0.0', port=port)
