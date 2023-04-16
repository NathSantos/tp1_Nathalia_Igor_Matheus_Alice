# ufam-db-tp1

Repositorio base para o Trabalho de Banco de Dados da Graduação em Ciencia da Computação na UFAM

## Copiando esse repositorio

Você deve ter uma conta no github, criar é gratis, e ele é essencial para a vida e carreira de você.

Para fazer isso siga esses passos:

https://user-images.githubusercontent.com/118348/229365938-48d261c8-b569-463c-bc00-462eb218b423.mp4

Para entender melhor [git e github](https://www.alura.com.br/artigos/o-que-e-git-github).

## Configurando

### Docker e Docker Compose

Instalando o [docker desktop e docker compose (Windows, Linux e Mac)](https://www.docker.com/products/docker-desktop/)

Instalando na linha de comando

[Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt) e [Docker Compose Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-pt)

#### Como funciona o docker compose

[Docker Compose - Explicado](https://blog.4linux.com.br/docker-compose-explicado/)

### Postgres

Criar pasta `postgres-data` na raiz do projeto. Essa pasta **não deve ser enviada** para o github.

Depois você deve subir o docker-compose com o postgres. Da primeira vez vai demorar um pouco, e fique de olho nos logs para qualquer erro.

```bash
docker-compose up -d
```

### Python

Criar o ambiente virtual

```bash
python3 -m venv .tp1
```

Ativar o ambiente virtual

```bash
source .tp1/bin/activate
```

## Usando o postgres na sua maquina

Após subir, você conseguirá conectar no banco. Ele vem vazio e você terá que preencher ele com o que o trabalho pede.

```bash
psql -h localhost -U postgres
```

As credenciais são:

```yaml
username: postgres
password: postgres
```

## Usando Python

Para instalar bibliotecas necessarias para o trabalho, use o pip [DEPOIS de ativar o ambiente](#python) virtual.

```bash
pip install <biblioteca>
```

# Scripts

- ```tp1_3.2.py``` -> Script contendo a extração dos dados, a criação do esquema do BD e o povoamento das relações
- ```tp1_3.3.py``` -> Script contendo o Dashboard com a execução das consultas

# Como executar os scripts

## Script tp1_3.2.py

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

## Script tp1_3.3.py

Para testar o script ```tp1_3.3.py``` que executará o Dashboard das consultas, ...
