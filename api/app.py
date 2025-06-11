from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'mensagem': 'API do Mini-Curso está rodando'}), 200
@app.route('/api/usets', methods=['POST'])

@app.route('/api/users', methods=['GET'])
def get_users():
     response = requests.get(f'https://jsonplaceholder.typicode.com/users')
     if response.status_code == 200:
        return jsonify(response.json()), 200
     
     return jsonify({'error' : 'Erro ao acessar api externa'}), response.status_code


# @GET - Listar todos os livros
@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros_memoria), 200

# POST - Adcionar livros
@app.route('/livros', methos=['POST'])
def adcionar_livros():
    dados = request.get_json()

    if not dados.get('titulo') or not dados.get('autor'):
        return jsonify({'erro': 'Titulo e autor sao obrigatorios'}), 400
    
    livro = {
        'id': len(livros_memoria) + 1,
        'titulo': dados['titulo'],
        'autor': dados['autor'],
        'ano': dados['ano'],
        'genero': dados['genero'],
    }
    livros_memoria.append(livro)
    return jsonify(livro), 201



# Put - atualizar livro
@app.route('livros/<int:id>', methods=['PUT'])
def atualizar_livros(id):
    dados = request.get_json
    for livro in livros_memoria:
        if livro['id'] == id:
            livro['titulo'] = dados.get('Titulo', livro['titulo'])
            livro['autor'] = dados.get('autor', livro['autor'])
            livro['ano'] = dados.get('ano', livro['ano'])
            livro['genero'] = dados.get('genero', livro['genero'])

            return jsonify(livro), 200
        return jsonify({'erro': 'Livro não encontrado'}), 404


# @DELETE - Deletar o livro

@app.route('/livros/<int:id>', methods={'DELETE'})
def deletar_livro(id):
    dados = request.get_json()
    for livro in livros_memoria:
        if livro['id'] == id:
            livros_memoria.remove(livro)
            return jsonify({'Mensagem': 'Livro removido com sucesso'}), 200
        return jsonify({'ero': 'livro não encontrado'}), 404


if __name__ == '__main__':
     app.run(debug=True)