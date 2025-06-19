from flask import Blueprint, request, jsonify
from .models import Student
from . import db

student_bp = Blueprint('students', __name__)

@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(name=data['name'], email=data['email'], course=data['course'])
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student created successfully'}), 201

@student_bp.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'email': s.email,
        'course': s.course
    } for s in students])

@student_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({
        'id': student.id,
        'name': student.name,
        'email': student.email,
        'course': student.course
    })

@student_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get_or_404(id)
    student.name = data['name']
    student.email = data['email']
    student.course = data['course']
    db.session.commit()
    return jsonify({'message': 'Student updated successfully'})

@student_bp.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'})
