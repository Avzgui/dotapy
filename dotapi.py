from flask import Flask, jsonify

app = Flask(__name__)

heroes = [
    {
        'id': 1,
        'name': u'Admiral',
        'surname': u'Daelin Proudmoore',
        'stats': u'Strenght'
    },
    {
        'id': 2,
        'name': u'Anti-Mage',
        'surname': u'Magina',
        'stats': u'Agility'
    }
]

@app.route('/api/v1.0/heroes', methods=['GET'])
def get_tasks():
    return jsonify({'heroes': heroes})

if __name__ == '__main__':
    app.run(debug=True)