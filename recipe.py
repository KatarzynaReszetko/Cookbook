import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cookbook (id serial PRIMARY KEY, recipe_name varchar, description varchar);")
conn.commit()


def add_recipe(name, desc):
    cur.execute("INSERT INTO cookbook (recipe_name, description) VALUES (%s, %s) RETURNING id", (name, desc))
    conn.commit()
    return cur.fetchone()[0]


def get_recipe_list():
    cur.execute("SELECT * FROM cookbook")
    result = cur.fetchall()
    return result


def get_recipe(id_recipe):
    cur.execute("SELECT recipe_name, description FROM cookbook WHERE id=%s", (id_recipe,))
    result = cur.fetchone()
    return result