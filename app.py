from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    
    ist = pytz.timezone('Asia/Kolkata')
    time_now = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
    html = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {time_now}</h3>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
