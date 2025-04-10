from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        nomes = request.form['nomes']
        lista_nomes = [nome.strip() for nome in nomes.strip().split('\n') if nome.strip()]
        if lista_nomes:
            resultado = random.choice(lista_nomes)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

