import unittest

from recipe_api import app


class APITesting(unittest.TestCase):
    def test_index_address(self):
        with app.test_client() as client:
            response = client.get('/')

        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(list, type(json_data))
        for recipe in json_data:
            self.assertEqual(len(recipe), 3)
            self.assertTrue('id' in recipe)
            self.assertTrue('description' in recipe)
            self.assertTrue('name' in recipe)

    def test_get_recipe(self):
        recipe_id = 1
        with app.test_client() as client:
            response = client.get(f'/{recipe_id}')

        json_data = response.get_json()
        self.assertEqual(dict, type(json_data))
        self.assertEqual(len(json_data), 3)
        self.assertTrue('id' in json_data)
        self.assertTrue('description' in json_data)
        self.assertTrue('name' in json_data)
        self.assertEqual(response.status_code, 200)

    def test_post_recipe(self):
        name = 'sernik'
        desc = 'z serem'
        with app.test_client() as client:
            response = client.post('/add', json={'name': name, 'desc': desc})

        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(dict, type(json_data))
        self.assertEqual(len(json_data), 1)
        self.assertTrue('id' in json_data)
        self.assertFalse('description' in json_data)
        self.assertFalse('name' in json_data)
