from flask import Flask, request
import requests
import os
import sys

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8356334314:AAF0R8Y1Vi7IOiCEIy8trmGFJnzbOb8RZlE"
TELEGRAM_CHAT_ID = "-1003423688594"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("=== WEBHOOK RECEIVED ===", file=sys.stderr, flush=True)
    try:
        content_type = request.content_type
        print(f"Content-Type: {content_type}", file=sys.stderr, flush=True)
        
        try:
            data = request.get_json(force=True, silent=True)
        except:
            data = None
        
        if data is None:
            data = request.data.decode('utf-8')
        
        print(f"Data received: {data}", file=sys.stderr, flush=True)
        
        if data:
            message = f"تنبيه من TradingView:\n\n{str(data)}"
        else:
            message = "تنبيه من TradingView"
        
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
        
        print(f"Sending to Telegram...", file=sys.stderr, flush=True)
        response = requests.post(telegram_url, json=payload, timeout=10)
        print(f"Telegram response: {response.status_code}", file=sys.stderr, flush=True)
        print(f"Response: {response.text}", file=sys.stderr, flush=True)
        
        if response.status_code == 200:
            print("Message sent successfully!", file=sys.stderr, flush=True)
        else:
            print(f"Failed to send: {response.text}", file=sys.stderr, flush=True)
        
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
