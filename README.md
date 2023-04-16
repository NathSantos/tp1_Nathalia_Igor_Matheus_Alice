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

Em seguida, no script ```tp1_3.2.py``` troque as variáveis do seguinte trecho de código, presente logo no início do código, de acordo com os seus dados:

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

Para testar o script ```tp1_3.3.py``` que executará o Dashboard das consultas, ...
