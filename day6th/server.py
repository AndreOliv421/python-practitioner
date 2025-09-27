# Flask | FastAPI

from flask import Flask, request, render_template, jsonify 

app  = Flask(__name__)

# rota de exemplo
@app.route('/helloword', methods=['GET'])
def helloword():
    return jsonify({
        "msg": "Ola mundo!"
    })

@app.route('/')
def home():
    return render_template(index.html)

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)
