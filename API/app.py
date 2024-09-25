from flask import Flask, request, jsonify, render_template  # Adicione render_template aqui
import requests

app = Flask(__name__)
livros = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/adicionar', methods=['POST'])
def adicionar_livro():
    data = request.json
    codigo = data.get('codigo')
    titulo = data.get('titulo')
    autor = data.get('autor')

    for livro in livros:
        if livro['codigo'] == codigo:
            return jsonify({'erro': 'Livro com esse código já existe.'}), 400

    novo_livro = {'codigo': codigo, 'titulo': titulo, 'autor': autor}
    livros.append(novo_livro)
    return jsonify({'mensagem': 'Livro adicionado com sucesso!'})

@app.route('/deletar', methods=['DELETE'])
def deletar_livro():
    data = request.json
    codigo = data.get('codigo')

    global livros
    livros = [livro for livro in livros if livro['codigo'] != codigo]
    return jsonify({'mensagem': 'Livro deletado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)  # Modo debug ativado