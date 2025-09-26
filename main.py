#Criar um banco de dados SQLite e uma tabela
import sqlite3

#Criar a conexão com o banco de dados chamado "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamado de "cursor" que será usado para executar os comandos sql
cursor = conexao.cursor()

#Criar uma tabela no banco
# cursor.execute("""
# CREATE TABLE  IF NOT EXISTS alunos (
#     id INTEGER  PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER NOT NULL,
#     curso TEXT            
#     )
# """)
#Pegando os dados com o input
# nome =  input("Digite o nome do aluno: ").lower()
# idade = int(input("Digite a idade do aluno:"))
# curso = input("Digite o curso do aluno: ").lower()

# #inserir um dado na tabela
# cursor.execute("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?,?,?)               
#  """,
# (nome, idade, curso)
                            
# )

# #Confirmar as alterações no banco
# conexao.commit()

# Inserir varios alunos de uma só vez
# alunos = [ 
#     ("Yago", 28, "Direito"),
#     ("Jessica", 27, "Computação"),
#     ("Breno", 52, "Computação"),
# ]
# #executemany permite inserir multiplas linhas de uma vez só
# cursor.executemany("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?,?,?)               
# """,
# (alunos)
# )
# conexao.commit()

#Atulizar dados no banco
# cursor.execute("""
# UPDATE alunos
# SET idade = ?, curso = ?
# WHERE id = ?                       
# """, (30, "ADS", 1)
# )
# conexao.commit()

#Funçao de listar dados no banco
#Cunsultar os dados nno banco
# cursor.execute(" SELECT * FROM alunos")

#Fetchall traz todos as linhas da consulta
# for linha in cursor.fetchall():
#     print(f"ID: {linha[0]} | Nome: {linha[1]} | idade: {linha[2]} | Curso: {linha[3]}")
# print("-"*50)

# pesquisar = input("Digite o curso que deseja pesquisar os alunos: ")
# cursor.execute(" SELECT nome, idade FROM alunos WHERE curso = ?", (pesquisar,))
# print(f"Alunos do curso de {pesquisar}")
# for linha in cursor.fetchall():
#     print(f"Nome: {linha[0]} | idade: {linha[1]}")

#Deletar dados no banco.
cursor.execute("Delete FROM alunos WHERE id = ?", (2,))
conexao.commit()

#Sempre fechar a conexão com o banco de dados
conexao.close()