from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "user1": {"username": "user1", "name": "John Doe", "age": 30, "city": "New York"},
    "user2": {"username": "user2", "name": "Jane Doe", "age": 25, "city": "Los Angeles"},
    "user3": {"username": "user3", "name": "Jim Doe", "age": 35, "city": "Chicago"}
}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json()
    username = new_user.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({"message": "User added successfully", "user": new_user}), 201

if __name__ == '__main__':
    app.run(port=5000)
