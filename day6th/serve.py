from flask import Flask, request, render_template, jsonify 

app = Flask(__name__)

# Rota de exemplo
@app.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "Olá mundo!"
    })

@app.route('/')
def home():
    return render_template('index.html')

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)