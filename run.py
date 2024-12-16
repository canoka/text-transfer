from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Basit bir depolama alanı (runtime boyunca)
shared_text = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_text():
    global shared_text
    data = request.json
    if 'text' in data:
        shared_text = data['text']
        return jsonify({"message": "Metin alındı."}), 200
    return jsonify({"error": "Metin gönderilmedi."}), 400

@app.route('/receive', methods=['GET'])
def receive_text():
    return jsonify({"text": shared_text}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
