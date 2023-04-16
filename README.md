# ufam-db-tp1

Repositório base para o 1o Trabalho de Banco de Dados da Graduação em Ciencia da Computação na UFAM

## Arquivos

- ```tp1_3.1.pdf``` -> Documentação do trabalho
- ```tp1_3.2.py``` -> Script contendo a extração dos dados, a criação do esquema do BD e o povoamento das relações
- ```tp1_3.3.py``` -> Script contendo o Dashboard com a execução das consultas
- ```classes.py``` -> Script contendo classes necessárias para a extração de dados **(esse arquivo é importado no script tp1_3.2.py)**
- ```requirements.txt``` -> Comandos ```pip install``` das bibliotecas necessárias

## Como executar os scripts

### Script tp1_3.2.py

Primeiro, crie um BD utilizando o pgAdmin ou o psql pelo terminal ```CREATE DATABASE nome_database;```

Em seguida, instale as bibliotecas presentes no arquivo ```requirements.txt```, necessárias para a execução dos códigos 

Após isso, no script ```tp1_3.2.py```, troque as variáveis do seguinte trecho de código, presente logo no início do código, de acordo com os seus dados:

```python
# Altere de acordo com seus dados
host="localhost"
nome_database="myowndatabase"
user="postgres"
password="2703"
```

- ```nome_database``` deve ser o nome do BD que você acabou de criar pelo pgAdmin ou pelo próprio terminal
- ```user``` deve ser o seu nome de usuário
- ```password``` deve ser a sua senha

Após ter feito isso, basta trocar a variável ```path_dir```, ainda no script ```tp1_3.2.py```, para conter o caminho do diretório para o arquivo de entrada ```amazon-meta.txt``` no seu computador:

```python3
path_dir = "C:\\Users\\naths\\Downloads\\Trabalho-1-BD\\amazon-meta.txt"

# Coloque aqui o diretório para o arquivo de entrada
with open(path_dir, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
```

Em seguida, já pode executar o código e a criação do esquema do BD, a extração de dados do arquivo de entrada e a população das relações já devem ocorrer corretamente.

Caso seja testado com o arquivo ```amazon-meta.txt``` completo, é normal que demore, dada a quantidade exorbitante de dados a serem extraídos.

### Script tp1_3.3.py

-----------------------------------------------------

**OBSERVAÇÃO IMPORTANTE!!!**

Temos uma relação chamada "Similar", que é uma palavra reservada do SQL. 

As consultas do dashboard já estão prontas para que o nome Similar não dê erro ao serem executadas:

```python
\"Similar\"
```

Entretando, **se as consultas forem testadas no pyAdmin**, por exemplo, devem apenas ser retirados as contra-barras presentes no nome Similar. Logo, ficaria da seguinte forma:

```SQL
"Similar"
```
-----------------------------------------------------

Para testar o script ```tp1_3.3.py``` que executará o Dashboard das consultas, primeiramente deve-se alterar os dados de ```host```, ```nome_database```, ```user``` e ```password``` conforme foi feito para a execução do ```tp1_3.2.py```.  

Em seguida, recomenda-se testar uma consulta por vez, comentando todas as outras que não estiverem sendo utilizadas no momento e deixando descomentada somente a que está sendo testada.

Após isso, basta ficar atento às questões ```A``` ```B``` e ```C```, que precisam ter o valor do ASIN alterado para o ASIN do produto que se deseja buscar.

Para facilitar esse processo, identificamos nessas 3 questões onde deve ser alterado para colocar o valor do ASIN desejado. Por exemplo:

```python3
# QUESTAO B - Dado um produto, listar os produtos similares com maiores vendas do que ele

# !!!! ---> MODIFIQUE AS LINHAS 59 E 60 NOS CAMPOS 'COLOQUE_ASIN_AQUI' DE ACORDO COM O PRODUTO QUE DESEJA BUSCAR
cur.execute('''SELECT MainTable.ASIN, MainTable.title, MainTable.salesrank 
                FROM MainTable 
                JOIN \"Similar\" s ON MainTable.ASIN = s.ASIN_similar 
                WHERE s.ASIN_original = 'COLOQUE_ASIN_AQUI' AND 
                MainTable.salesrank > (SELECT salesrank FROM MainTable WHERE ASIN = 'COLOQUE_ASIN_AQUI')
                ORDER BY MainTable.salesrank ASC;'''
)
```
