import psycopg2

# conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
conn = psycopg2.connect("dbname=d2bv9lgh3mb7gh user=muonbpxbpohall host=ec2-54-146-91-153.compute-1.amazonaws.com password=18b8fe0e5f24688845973077487fda0d030d632f1b5f5e8c053270c0a478e2a6")
cur = conn.cursor()
try:
    cur.execute("CREATE TABLE IF NOT EXISTS cookbook (id serial PRIMARY KEY, recipe_name varchar, ingredients varchar, instructions varchar, photo varchar);")
except:
    pass
conn.commit()


def add_recipe(name, ingr, instr, photo):
    cur.execute("INSERT INTO cookbook (recipe_name, ingredients, instructions, photo) VALUES (%s, %s, %s, %s) RETURNING id", (name, ingr, instr, photo))
    conn.commit()
    return cur.fetchone()[0]


def get_recipe_list():
    cur.execute("SELECT * FROM cookbook")
    result = cur.fetchall()
    print(result)
    return result


def get_recipe(id_recipe):
    cur.execute("SELECT recipe_name, ingredients, instructions, photo FROM cookbook WHERE id=%s", (id_recipe,))
    result = cur.fetchone()
    print(result)
    return result