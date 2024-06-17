import os
from dataclasses import dataclass

os.system('cls || clear')

QUANTIDADE_LIVROS = 2

@dataclass
class Livro:
    titulo: str
    autor: str
    numeroDePaginas: int
    preco: float

livros = []

for i in range(QUANTIDADE_LIVROS):

    titulo = input('Digite o nome do livro: ')
    autor = input('Digite o nome do autor: ')
    numeroDePaginas = int(input('Digite a quantidade de páginas: '))
    preco = float(input('Digite o preço do livro: '))
    
    livro = Livro(titulo = titulo, autor = autor, numeroDePaginas = numeroDePaginas, preco = preco)
    livros.append(livro)

for dados_livro in livros:
    print(f'Titulo: {dados_livro.titulo}')
    print(f'Autor: {dados_livro.autor}')
    print(f'Numero de páginas: {dados_livro.numeroDePaginas}')
    print(f'Preço do livro: {dados_livro.preco}')
