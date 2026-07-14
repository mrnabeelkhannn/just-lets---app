from flask import Flask, request, jsonify
import razorpay
import requests

app = Flask(__name__)

# 1. Apni Keys
RAZORPAY_KEY_ID = "YOUR_RAZORPAY_KEY_ID_HERE"
RAZORPAY_KEY_SECRET = "YOUR_ROZARPAY_KEY_SECRET_HERE"
DEEPSEEK_API_KEY = "YOUR_API_KEY_HERE"

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

@app.route('/')
def home():
    return "Just Lets Backend is Running Safely!"

# 2. PAYMENT ROUTE
@app.route('/create_order', methods=['POST'])
def create_order():
    try:
        data = request.json
        amount = data.get('amount')
        options = {
            "amount": amount,
            "currency": "INR",
            "receipt": "order_rcptid_11"
        }
        order = client.order.create(data=options)
        return jsonify({"status": "success", "order": order})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# 3. AI ROUTE
@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    try:
        data = request.json
        user_message = data.get('message')
        
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": user_message}]
        }
        
        response = requests.post("https://api.deepseek.com/v1/chat/completions", json=payload, headers=headers)
        ai_response = response.json()
        
        return jsonify({"status": "success", "reply": ai_response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)