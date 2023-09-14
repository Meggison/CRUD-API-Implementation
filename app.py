from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

with app.app_context():
    db.create_all()

@app.route('/api/person', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully'}), 201

@app.route('/api/person/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)
    if person:
        return jsonify({'name': person.name})
    return jsonify({'error': 'Person not found'}), 404

@app.route('/api/person/<int:id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    data = request.get_json()
    new_name = data.get('name')

    if not new_name:
        return jsonify({'error': 'Name is required'}), 400

    person.name = new_name
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

@app.route('/api/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})

if __name__ == '__main__':
    app.run()
