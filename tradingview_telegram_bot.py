from flask import Flask, request
import requests
import os

app = Flask(*name*)

# ضع معلوماتك هنا

TELEGRAM_BOT_TOKEN = "8356334314:AAF0R8Y1Vi7IOiCEIy8trmGFJnzbOb8RZlE"  # Token من BotFather
TELEGRAM_CHAT_ID = "-1003423688594"  # Chat ID حقك

@app.route(’/webhook’, methods=[‘POST’])
def webhook():
try:
# استقبال البيانات من TradingView
data = request.get_json()


    # تحويل البيانات لرسالة
    if data:
        message = f"🔔 تنبيه من TradingView:\n\n{data}"
    else:
        message = "تنبيه من TradingView (بدون بيانات)"
    
    # إرسال الرسالة للتليجرام
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    
    response = requests.post(telegram_url, json=payload)
    
    return {"status": "success"}, 200

except Exception as e:
    print(f"Error: {e}")
    return {"status": "error", "message": str(e)}, 500


@app.route(’/’)
def home():
return “TradingView to Telegram Bot is running! ✅”

if *name* == ‘*main*’:
port = int(os.environ.get(‘PORT’, 5000))

app.run(host=‘0.0.0.0’, port=port)
