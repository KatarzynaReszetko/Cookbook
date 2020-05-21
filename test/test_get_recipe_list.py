import unittest
import psycopg2
from recipe import add_recipe, get_recipe_list


class Testing(unittest.TestCase):
    def test_get_recipe_list(self):
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
        cur = conn.cursor()
        name1 = "Sałatka grecka"
        name2 = "Pulpeciki w sosie pomidorowym"
        name3 = "Zapiekanka z brokułami"
        desc1 = "dużo sera feta"
        desc2 = "aleee pomidorowo"
        desc3 = "zielono mi"
        cur.execute("SELECT COUNT (*) FROM cookbook")
        quantity_before_adding = cur.fetchone()[0]
        print()
        print('quantity before adding:', quantity_before_adding)
        result_before_adding = get_recipe_list()
        print()
        print('result before adding:', result_before_adding)
        id_added_recipe1 = add_recipe(name1, desc1)
        id_added_recipe2 = add_recipe(name2, desc2)
        id_added_recipe3 = add_recipe(name3, desc3)
        print('added id:', id_added_recipe1, id_added_recipe2, id_added_recipe3)

        cur.execute("SELECT COUNT (*) FROM cookbook")
        quantity_after_adding = cur.fetchone()[0]
        print('quantity after adding:', quantity_after_adding)
        result_after_adding = get_recipe_list()
        print('result after adding:', result_after_adding)

        for recipe in result_after_adding:
            self.assertEqual(len(recipe), 3)

        recipe1 = (id_added_recipe1, name1, desc1)
        self.assertTrue(recipe1 in result_after_adding)

        self.assertEqual(quantity_after_adding - quantity_before_adding, 3)

        cur.execute("DELETE FROM cookbook WHERE id=%s", (id_added_recipe1,))
        cur.execute("DELETE FROM cookbook WHERE id=%s", (id_added_recipe2,))
        cur.execute("DELETE FROM cookbook WHERE id=%s", (id_added_recipe3,))
        conn.commit()
                                                                              
        cur.execute("SELECT COUNT (*) FROM cookbook")
        quantity_after_cleaning = cur.fetchone()[0]
        
        result_after_cleaning = get_recipe_list()

        self.assertEqual(quantity_before_adding, quantity_after_cleaning)
        
        print('quantity after cleaning:', quantity_after_cleaning)
        print('result after cleaning:', result_after_cleaning)

        
if __name__ == '__main__':
        unittest.main(verbosity=2)
