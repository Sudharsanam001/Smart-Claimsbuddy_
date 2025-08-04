from flask import Flask, request, render_template
import requests

app = Flask(__name__)

INYA_API_URL = "https://api.inya.ai/v1/query"  # Replace if different
API_KEY = "Bearer YOUR_API_KEY"  # Replace this
AGENT_ID = "5950e0def8cb418e99174289dfcbcd67"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_claim():
    file = request.files['file']
    files = {'file': (file.filename, file.read())}
    data = {
        "agent_id": AGENT_ID,
        "message": "Please process this claim."
    }
    headers = {
        "Authorization": API_KEY
    }
    response = requests.post(INYA_API_URL, headers=headers, data=data, files=files)
    result = response.json()

    return f"""
    <h3>Decision: {result.get("Decision", "N/A")}</h3>
    <p>Reason: {result.get("Reason", "No reason given")}</p>
    <a href="/">Back</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
