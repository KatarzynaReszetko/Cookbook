import psycopg2

# conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
conn = psycopg2.connect("dbname=d5voqb9qc5gnc2 user=oumicejvjspnog host=ec2-52-204-232-46.compute-1.amazonaws.com password=e21795e43497d5e99097d2b6a1dc0f1efd38b2f78a2ac1ec0b5fd4b170877834")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cookbook (id serial PRIMARY KEY, recipe_name varchar, description varchar);")
conn.commit()


def add_recipe(name, desc, photo):
    cur.execute("INSERT INTO cookbook (recipe_name, description, photo) VALUES (%s, %s, %s) RETURNING id", (name, desc, photo))
    conn.commit()
    return cur.fetchone()[0]


def get_recipe_list():
    cur.execute("SELECT * FROM cookbook")
    result = cur.fetchall()
    return result


def get_recipe(id_recipe):
    cur.execute("SELECT recipe_name, description, photo FROM cookbook WHERE id=%s", (id_recipe,))
    result = cur.fetchone()
    return result