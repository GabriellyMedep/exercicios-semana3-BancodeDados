import sqlite3

conexao = sqlite3.connect('clientes')
cursor = conexao.cursor()

cursor.execute("CREATE TABLE clientes(id INT primary key, nome VARVHAR(200), idade INT, saldo FLOAT);")

cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, 'João', '40', 1500)")
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, 'Ana', '35', 1000)")
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, 'Daniel', '43', 2000)")
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, 'Mariana', '20', 1100)")
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, 'Carol', '50', 1600)")

# Nome e idade > 30 anos
dados = cursor.execute("SELECT nome, idade FROM clientes WHERE idade >= 30")

# Saldo médio dos clientes
dados = cursor.execute("SELECT AVG (saldo) FROM clientes")

# Cliente com saldo máximo
dados = cursor.execute("SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)")

# Quantidade de clientes com saldo > 1000
dados = cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo >= 1000")

# Atualizar saldo
dados = cursor.execute("UPDATE clientes SET saldo = 2000 WHERE id = 1")

# Remover cliente pelo id
dados = cursor.execute("DELETE FROM clientes WHERE id = 2")

# Junção de tabelas

cursor.execute(""" CREATE TABLE compras(
    id INT PRIMARY KEY, 
   cliente_id INT, 
    produto VARCHAR(250), 
   valor FLOAT,
   CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);""")

dados = cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 4, 'Casaco', 150)")
dados = cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES(6, 5, 'Camisa', 19.90)")
dados = cursor.execute("INSERT INTO compras(id, cliente_id, produto, valor) VALUES(5, 6, 'Calça', 179.90)")

# Nome, produto e valor de cada compra
dados = cursor.execute("SELECT c.nome, co.produto, co.valor FROM compras as co INNER JOIN clientes as c ON c.id = co.cliente_id")

dados = cursor.execute("SELECT * FROM compras")

for item in dados:
    print(item)

conexao.commit()
conexao.close()


