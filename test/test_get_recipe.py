import unittest
import psycopg2
from recipe import add_recipe, get_recipe


class Testing(unittest.TestCase):
    def test_get_recipe(self):
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
        cur = conn.cursor()
        name = 'Tort malinowy'
        desc = 'Bardzo słodko'
        cur.execute("SELECT COUNT (*) FROM cookbook")
        result_before_adding = cur.fetchone()[0]
        print()
        print('result before adding:', result_before_adding)
        id_added_recipe = add_recipe(name, desc)
        print('added id:', id_added_recipe)
        
        returned_name, returned_desc = get_recipe(id_added_recipe)
        print('returned:', returned_name, returned_desc)

        self.assertEqual(name, returned_name)
        self.assertEqual(desc, returned_desc)

        cur.execute("DELETE FROM cookbook WHERE id=%s", (id_added_recipe,))
        cur.execute("SELECT COUNT (*) FROM cookbook")
        result_after_cleaning = cur.fetchone()[0]

        self.assertEqual(result_before_adding, result_after_cleaning)

        print('result after cleaning:', result_after_cleaning)

        
if __name__ == '__main__':
        unittest.main(verbosity=2)
