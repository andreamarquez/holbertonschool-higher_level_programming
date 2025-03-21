import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    # Read data from items.json
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get("items", [])  # Default to an empty list if "items" is missing
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
