from flask import Flask, jsonify, request
from flask_cors import CORS

from recipe import add_recipe, get_recipe_list, get_recipe

app = Flask(__name__)
CORS(app)

HEADERS = {'Access-Control-Allow-Origin': '*'}


@app.route('/')
def recipe_list():
    result = []
    for recipe in get_recipe_list():
        recipe_dict = dict(
            id=recipe[0],
            name=recipe[1],
            description=recipe[2]
        )
        result.append(recipe_dict)
    return jsonify(result), 200, HEADERS


@app.route('/<int:id_recipe>')
def recipe_details(id_recipe):
    recipe = get_recipe(id_recipe)
    recipe_dict = dict(
        id=id_recipe,
        name=recipe[0],
        description=recipe[1]
    )
    return jsonify(recipe_dict), 200, HEADERS


@app.route('/add', methods=['POST'])
def recipe_id():
    name = request.json['name']
    desc = request.json['desc']
    id_recipe = add_recipe(name, desc)
    return jsonify({'id': id_recipe}), 201, HEADERS


if __name__ == '__main__':
    app.run(debug=True)
