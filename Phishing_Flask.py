from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

# Log file to store click data
LOG_FILE = "click_log.txt"

@app.route('/phish')
def track_click():
    user_ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] Clicked from IP: {user_ip}\n")

    print(f"[LOG] Click tracked: {user_ip} at {timestamp}")
    # Redirect to safe landing page or awareness article
    return redirect("https://www.phishing.org/what-is-phishing")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)