import requests

url_auth = 'https://www.mauricio.app.br/p6/bib/authenticate.php'
url_list = 'https://mauricio.app.br/p6/bib/list.php'
url_add = 'https://mauricio.app.br/p6/bib/add.php'
url_del = 'https://mauricio.app.br/p6/bib/del.php'

def autenticar():
    credentials = {
        'username': 'aluno',
        'password': 'password'
    }

    response = requests.post(url_auth, data=credentials)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    
    if response.status_code == 200:
        response_data = response.json()
        print(f"Response JSON: {response_data}")
        token = response_data.get('token')  # Verifica se a chave '

def listar_livros(token, codigo=None):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    params = {}
    if codigo:
        params['codigo'] = codigo
    
    response = requests.get(url_list, headers=headers, params=params)
    
    if response.status_code == 200:
        livros = response.json()
        print('Livros encontrados:', livros)
    else:
        print(f'Erro ao listar livros: {response.text}')

# Função para adicionar um livro, o token vai aqui, após a funçao f'Bearer , entre as chaves {}
def adicionar_livro(token, codigo, titulo, autor):
    headers = {
        'Authorization': f'Bearer {'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3MjcyODM3ODIsImp0aSI6IlRJY0Z2ZXRUTGpsUXlIRlpFREdFMHc9PSIsImlzcyI6Ind3dy5tYXVyaWNpby5hcHAuYnIiLCJuYmYiOjE3MjcyODM3ODIsImV4cCI6MTcyNzI5MDk4MiwiZGF0YSI6eyJ1c2VyTmFtZSI6ImFsdW5vIn19.VBFmNqTRPr3p7mGy3tZdzEbQj6DkbMjtPz0gEG3TdnHMOGUslAdYV2YydW38OAVp-0DaGl-mknbKcPtFoSiOKg'}'
    }
    
    data = {
        'codigo': codigo,
        'titulo': titulo,
        'autor': autor
    }
    
    response = requests.post(url_add, headers=headers, data=data)
    
    if response.status_code == 200:
        print('Livro adicionado com sucesso!')
    else:
        print(f'Erro ao adicionar livro: {response.text}')

def deletar_livro(token, codigo):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    data = {
        'codigo': codigo
    }
    
    response = requests.post(url_del, headers=headers, data=data)
    
    if response.status_code == 200:
        print('Livro deletado com sucesso!')
    else:
        print(f'Erro ao deletar livro: {response.text}')

if __name__ == "__main__":
    token = autenticar()
    
    if token:
        # Listar todos os livros
        print("\nListando todos os livros:")
        listar_livros(token)
        
        # Adicionar um livro
        print("\nAdicionando um novo livro:")
        adicionar_livro(token, 123, 'Introdução à Programação com Python', 'Maria Oliveira')
        
        # Listar o livro adicionado
        print("\nListando o livro adicionado (código 123):")
        listar_livros(token, codigo=123)
        
        # Deletar o livro
        print("\nDeletando o livro com código 123:")
        deletar_livro(token, 123)
        
        # Listar novamente para confirmar a exclusão
        print("\nListando novamente para confirmar exclusão:")
        listar_livros(token)
