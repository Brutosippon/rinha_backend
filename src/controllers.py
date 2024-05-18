from flask import request, jsonify, Blueprint
from models import db, Person
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

person_bp = Blueprint('person_bp', __name__)

@person_bp.route('/pessoas', methods=['POST'])
def create_person():
    data = request.get_json()   
    try:
        person = Person(
            nome=data.get['nome'], 
            apelido=data.get['apelido'], 
            nascimento=data.get['nascimento'], 
            stack=data.get['stack', []]
        )
        db.session.add(person)
        db.session.commit()
        return jsonify(person.id), 201, {'Location': f'/pessoas/{person.id}'}
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Apelido must be unique'}), 422
    except KeyError:
        return jsonify({'error': 'Bad request'}), 400
    #except Exception as e:
        #return jsonify({'message': f'An error occurred: {e}'}), 500
    
@person_bp.route('/pessoas/<uuid:id>', methods=['GET'])
def get_person(id):
    try:
        person = Person.query.filter_by(id=id).one()
        return jsonify({
            'id': str(person.id),
            'nome': person.nome,
            'apelido': person.apelido,
            'nascimento': person.nascimento.strftime('%Y-%m-%d'), #isoformat()
            'stack': person.stack
        }),200
    except NoResultFound:
        return jsonify({'error': 'Person not found'}), 404
    #except Exception as e:
        #return jsonify({'message': f'An error occurred: {e}'}), 500

@person_bp.route('/pessoas', methods=['GET'])
def search_person():
    term =  request.args.get('t')
    if not term:
        return jsonify({'error': 'Search term is required'}), 400
    
    persons = Person.query.filter(
        (Person.nome.ilike(f'%{term}%')) | 
        (Person.apelido.ilike(f'%{term}%')) |
        (Person.stack.any(term))
    ).limit(50).all()
    
    return jsonify([{
        'id': str(person.id),
        'nome': person.nome,
        'apelido': person.apelido,
        'nascimento': person.nascimento.strftime('%Y-%m-%d'), #isoformat()
        'stack': person.stack
    } for person in persons]), 200

@person_bp.route('/contagem-pessoas', methods=['GET'])
def count_person():
    count = Person.query.count()
    return str(count), 200