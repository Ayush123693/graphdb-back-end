# app.py (Flask)
from flask import Flask, config, request, jsonify
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define SQL database models
class Namespace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

@app.route('/connect-to-blazegraph', methods=['GET'])
def connect_to_blazegraph():
    # Connect to BlazeGraph logic
    return jsonify({"message": "Connected to BlazeGraph"})

@app.route('/create-database', methods=['POST'])
def create_database():
    github_link = 'https://github.com/blazegraph'  # Using the BlazeGraph GitHub link
    # Create database from GitHub link logic
    return jsonify({"message": "Database created from GitHub link"})

@app.route('/add-namespace', methods=['POST'])
def add_namespace():
    namespace_name = request.json.get('namespace')
    new_namespace = Namespace(name=namespace_name)
    db.session.add(new_namespace)
    db.session.commit()
    return jsonify({"message": f"Added new namespace: {namespace_name}"})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)