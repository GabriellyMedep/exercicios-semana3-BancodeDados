# Exercícios Banco de Dados

import sqlite3

conexao = sqlite3.connect('alunos')
cursor = conexao.cursor()

cursor.execute("CREATE TABLE alunos(id INT, nome VARVHAR(200), idade INT, curso VARCHAR(200));")

cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(1, 'Gabrielly', '20', 'Python')")
cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(2, 'João', '30', 'Matemática')")
cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(3, 'Daniela', '28', 'História')")
cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(4, 'Mariana', '22', 'Dados')")
cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(5, 'Ana', '25', 'Python')")


# Filtrando todos os alunos
dados = cursor.execute("SELECT * FROM alunos")

# Filtrando alunos com mais de 20 anos
dados = cursor.execute("SELECT nome, idade FROM alunos WHERE idade > 20")

# Colocaando em ordem alfabética somente alunos que cursam Engenharia
dados = cursor.execute("SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")

# Total de alunos
dados = cursor.execute("SELECT count(*) FROM alunos")

# Atualizando a idade
dados = cursor.execute("UPDATE alunos SET idade = 28 WHERE id = 1")

#Removendo um aluno
dados = cursor.execute("DELETE FROM alunos WHERE id = 5")

for alunos in dados:
    print(alunos)

conexao.commit()
conexao.close()