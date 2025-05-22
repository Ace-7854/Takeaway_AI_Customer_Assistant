from flask import Flask, render_template, request, redirect, url_for, session

from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        session['user'] = {
            'email':email,
            'pwrd' : password
        }

        if email == "email@test.com" and password == "pass123":
            return render_template(url_for('dashboard'))
        
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    
    return render_template(
        'dashboard.html',
        user=session['user']
        )



@app.route('/webhook', methods=['POST'])
def receive_webhook():
    # Get JSON data sent by Bland AI
    data = request.get_json()

    # Just print it for now (you can store it or process it later)
    print("Received webhook data:", data)

    # Example: Accessing specific fields if you're using analysis_schema
    customer_name = data.get("customer_name")
    order_items = data.get("order_items")

    print(f"Order from {customer_name}: {order_items}")

    # Return a success response to Bland AI
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
