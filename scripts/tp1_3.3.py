import psycopg2

# =================================================================================================
#
#                               DASHBOARD DE CONSULTAS
#
# =================================================================================================

# Crie um BD utilizando o pgAdmin ou o psql pelo terminal com o seguinte comando:
# CREATE DATABASE nome_database;

# Altere de acordo com seus dados
host="localhost"
nome_database="myowndatabase"
user="postgres"
password="2703"

# Conecta com o BD criado
conn = psycopg2.connect("host=" + host +
                        " dbname=" + nome_database +
                        " user=" + user +
                        " password=" + password)

# Abre um cursor para fazer operações no BD
cur = conn.cursor()

# QUESTAO A - Dado um produto, listar os 5 comentários mais úteis e com maior avaliação e 
# os 5 comentários mais úteis e com menor avaliação

# !!!! ---> MODIFIQUE AS LINHAS 33, 36, 43 E 46 NOS CAMPOS 'COLOQUE_ASIN_AQUI' DE ACORDO COM O PRODUTO QUE DESEJA BUSCAR
cur.execute('''(SELECT r.rating, r.helpful, r.customer, r.data, r.asin_original
            FROM Reviews r
            WHERE r.asin_original = 'COLOQUE_ASIN_AQUI' AND r.id NOT IN (
                SELECT r2.id
                FROM Reviews r2
                WHERE r2.asin_original = 'COLOQUE_ASIN_AQUI'
                ORDER BY r2.rating DESC, r2.helpful DESC
                LIMIT 5
            )ORDER BY r.rating DESC, r.helpful DESC LIMIT 5)
            UNION
            (SELECT r.rating, r.helpful, r.customer, r.data, r.asin_original
            FROM Reviews r
            WHERE r.asin_original = 'COLOQUE_ASIN_AQUI' AND r.id NOT IN (
                SELECT r2.id
                FROM Reviews r2
                WHERE r2.asin_original = 'COLOQUE_ASIN_AQUI'
                ORDER BY r2.rating ASC, r2.helpful DESC
                LIMIT 5
            )ORDER BY r.rating ASC, r.helpful DESC LIMIT 5);'''
)


# QUESTAO B - Dado um produto, listar os produtos similares com maiores vendas do que ele

# !!!! ---> MODIFIQUE AS LINHAS 59 E 60 NOS CAMPOS 'COLOQUE_ASIN_AQUI' DE ACORDO COM O PRODUTO QUE DESEJA BUSCAR
cur.execute('''SELECT MainTable.ASIN, MainTable.title, MainTable.salesrank 
                FROM MainTable 
                JOIN \"Similar\" s ON MainTable.ASIN = s.ASIN_similar 
                WHERE s.ASIN_original = 'COLOQUE_ASIN_AQUI' AND 
                MainTable.salesrank > (SELECT salesrank FROM MainTable WHERE ASIN = 'COLOQUE_ASIN_AQUI')
                ORDER BY MainTable.salesrank ASC;'''
)


# QUESTAO C - Dado um produto, mostrar a evolução diária das médias de avaliação ao longo do 
# intervalo de tempo coberto no arquivo de entrada

# !!!! ---> MODIFIQUE A LINHA 71 NO CAMPO 'COLOQUE_ASIN_AQUI' DE ACORDO COM O PRODUTO QUE DESEJA BUSCAR
cur.execute('''SELECT r.data, AVG(r.rating) OVER (ORDER BY r.data) AS media_rating
                    FROM Reviews r
                    WHERE r.ASIN_original = 'COLOQUE_ASIN_AQUI'
                    ORDER BY r.data ASC;'''
)


# QUESTAO D - Listar os 10 produtos líderes de venda em cada grupo de produtos
cur.execute('''SELECT id, asin, title, grupo, salesrank, quant_categories
                FROM (
                SELECT id, asin, title, grupo, salesrank, quant_categories,
                        ROW_NUMBER() OVER (PARTITION BY grupo ORDER BY salesrank DESC) AS rn
                FROM MainTable
                ) ranked
                WHERE rn <= 10
                ORDER BY grupo, salesrank DESC'''
)


# QUESTAO E - Listar os 10 produtos com a maior média de avaliações úteis positivas por produto
cur.execute('''SELECT rg.asin_original, rg.total, rg.avg_rating, 
                    SUM(r.votes) AS total_votes, SUM(r.helpful) AS total_helpful, 
                    AVG(r.helpful) AS avg_helpful_per_review
                FROM Reviews r
                INNER JOIN ReviewsGeneralInfos rg ON r.asin_original = rg.asin_original
                WHERE r.rating > 3
                GROUP BY rg.asin_original, rg.total, rg.avg_rating
                ORDER BY avg_helpful_per_review DESC
                LIMIT 10'''
)


# QUESTAO F - Listar as 5 categorias de produto com a maior média de avaliações úteis positivas por produto
cur.execute('''SELECT c.id_categoria, allc.nome_categoria,
                    SUM(r.votes) AS total_votes, SUM(r.helpful) AS total_helpful, 
                    AVG(r.helpful) AS avg_helpful_per_review
                FROM Reviews r
                INNER JOIN ReviewsGeneralInfos rg ON r.asin_original = rg.asin_original
                INNER JOIN Categories c ON r.asin_original = c.asin_original
				INNER JOIN AllCategories allc ON c.id_categoria = allc.id_categoria
                WHERE r.rating > 3
                GROUP BY c.id_categoria, allc.nome_categoria
                ORDER BY avg_helpful_per_review DESC
                LIMIT 5'''
)


# QUESTAO G - Listar os 10 clientes que mais fizeram comentários por grupo de produto
cur.execute('''WITH top_reviewers AS (
                SELECT mt.grupo AS categoria, r.customer, COUNT(*) AS num_comentarios,
                    ROW_NUMBER() OVER (PARTITION BY mt.grupo ORDER BY COUNT(*) DESC) AS rn
                FROM MainTable mt
                JOIN Reviews r ON mt.ASIN = r.ASIN_original
                GROUP BY mt.grupo, r.customer)
            SELECT categoria, customer, num_comentarios
            FROM top_reviewers
            WHERE rn <= 10
            ORDER BY categoria, num_comentarios DESC;'''
)

# printa todos os resultados de uma consulta
x = cur.fetchall()
print(x)

# Fecha a conexão
cur.close()
conn.close()