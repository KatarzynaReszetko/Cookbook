import unittest
import psycopg2
from recipe import add_recipe


class Testing(unittest.TestCase):
    def test_add_recipe(self):
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
        cur = conn.cursor()
        name = 'Pierogi ruskie'
        desc = 'smaczne'
        cur.execute("SELECT COUNT (*) FROM cookbook WHERE recipe_name=%s AND description=%s", (name, desc))
        result_before = cur.fetchone()[0]

        print('result before:', result_before)

        recipe_id = add_recipe(name, desc)

        cur.execute("SELECT COUNT (*) FROM cookbook WHERE recipe_name=%s AND description=%s", (name, desc))
        result_after = cur.fetchone()[0]
        expected_elements_added = 1

        print('result after:', result_after)

        self.assertEqual(result_after - result_before, expected_elements_added)

        cur.execute("DELETE FROM cookbook WHERE id=%s", (recipe_id,))
        cur.execute("SELECT COUNT (*) FROM cookbook WHERE recipe_name=%s AND description=%s", (name, desc))
        result_after_cleaning = cur.fetchone()[0]

        self.assertEqual(result_before, result_after_cleaning)

        print('result after cleaning:', result_after_cleaning)


if __name__ == '__main__':
    unittest.main(verbosity=2)
