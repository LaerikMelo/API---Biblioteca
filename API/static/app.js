// Função para listar livros
function listarLivros() {
    fetch('/listar')  // Fazendo uma requisição GET para a rota '/listar'
        .then(response => response.json())  // Converte a resposta para JSON
        .then(data => {
            const lista = document.getElementById('livros-lista');  // Elemento onde os livros serão exibidos
            lista.innerHTML = '';  // Limpando a lista de livros

            // Verifica se a resposta é um array de livros
            if (Array.isArray(data)) {
                data.forEach(livro => {  // Itera sobre os livros e os exibe
                    const li = document.createElement('li');
                    li.textContent = `${livro.codigo} - ${livro.titulo} por ${livro.autor}`;
                    lista.appendChild(li);
                });
            } else {
                lista.innerHTML = `<li>${data.erro || 'Erro ao listar livros'}</li>`;
            }
        })
        .catch(error => console.error('Erro ao listar livros:', error));  // Tratamento de erro
}

// Função para adicionar um livro
function adicionarLivro() {
    const codigo = document.getElementById('codigo').value;
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;

    // Verifica se todos os campos estão preenchidos
    if (!codigo || !titulo || !autor) {
        document.getElementById('adicionar-mensagem').textContent = 'Por favor, preencha todos os campos';
        return;
    }

    // Faz uma requisição POST para a rota '/adicionar' com os dados do livro
    fetch('/adicionar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ codigo: codigo, titulo: titulo, autor: autor })
    })
    .then(response => response.json())
    .then(data => {
        // Exibe uma mensagem de sucesso ou erro
        document.getElementById('adicionar-mensagem').textContent = data.mensagem || data.erro;

        // Limpa os campos de entrada após a adição
        document.getElementById('codigo').value = '';
        document.getElementById('titulo').value = '';
        document.getElementById('autor').value = '';
        
        // Atualiza a lista de livros após adicionar
        listarLivros();
    })
    .catch(error => console.error('Erro ao adicionar livro:', error));  // Tratamento de erro
}

// Função para deletar um livro
function deletarLivro() {
    const codigo = document.getElementById('codigo-deletar').value;

    // Verifica se o campo código está preenchido
    if (!codigo) {
        document.getElementById('deletar-mensagem').textContent = 'Por favor, insira o código do livro a ser deletado';
        return;
    }

    // Faz uma requisição DELETE para a rota '/deletar' com o código do livro
    fetch('/deletar', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ codigo: codigo })
    })
    .then(response => response.json())
    .then(data => {
        // Exibe uma mensagem de sucesso ou erro
        document.getElementById('deletar-mensagem').textContent = data.mensagem || data.erro;

        // Limpa o campo de entrada
        document.getElementById('codigo-deletar').value = '';
        
        // Atualiza a lista de livros após deletar
        listarLivros();
    })
    .catch(error => console.error('Erro ao deletar livro:', error));  // Tratamento de erro
}
