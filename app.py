from flask import Flask, request, jsonify

app = Flask(__name__)

CORRECT_PASSWORD = "secretCTFpass"
FLAG = "flag{server_side_flag_ftw}"

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    if data.get("password") == CORRECT_PASSWORD:
        return jsonify({"status": "success", "flag": FLAG})
    return jsonify({"status": "fail", "message": "Wrong password"}), 401

# GET route that shows password only if User-Agent is curl
@app.route('/check', methods=['GET'])
def get_password():
    user_agent = request.headers.get('User-Agent', '')
    if "curl" in user_agent.lower():
        return jsonify({"CORRECT_PASSWORD": CORRECT_PASSWORD})
    else:
        return jsonify({"message": "Access Denied"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
