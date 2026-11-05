livros = [
{
    "id": 1,
    "titulo": "Python Fluente", # str
    "autor": "Luciano Ramalho", # str
    "ano": 2022,  #Imt
    "disponivel": True # bool - situações sim/não
},
{
    "id": 2,
    "titulo": "Flask Web Development", # str
    "autor": "Miguel Grinberg", # str
    "ano": 2018,  #Imt
    "disponivel": False # bool - situações sim/não
},
{
    "id": 3,
    "titulo": "Automatize Tarefas Maçantes com Python", # str
    "autor": "Al Sweigart", #str
    "ano": 2019,    #Imt
    "disponivel": True # bool - situações sim/não
}
]

# Parte 2 — Exibindo os livros
for livro in livros:
print(["id", "titulo", "autor"])


# Parte 3 — Filtrando livros disponiveis
for livro in livros:
    if livro["disponivel"]:
print(livro["titulo"])

# Parte 4 — Contando livros
quantidade_disponiveis = 0
for livro in livros:
    if livro["disponivel"]:
        quantidade_disponiveis += 1
print(livro"Livros Disponiveis:" quantidade_disponiveis)

# Parte 5 — Consultando por ID


# Parte 6 — Alterando um registro
novo_livro + livrp {"id": 4, "titulo": "Programacao Python", "autor": "Autor da turma", "ano": 2026, "disponivel": True}

Livros.append(novo_livro)