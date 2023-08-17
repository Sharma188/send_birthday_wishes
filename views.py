from flask import jsonify
from app import app
from models import Employee, Event, EmailTemplate


@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    event_list = [{'id': event.id, 'event_type': event.event_type, 'event_date': event.event_date} for event in events]
    return jsonify({'events': event_list})


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    employee_list = [{'id': emp.id, 'name': emp.name, 'email': emp.email} for emp in employees]
    return jsonify({'employees': employee_list})


@app.route('/templates', methods=['GET'])
def get_templates():
    templates = EmailTemplate.query.all()
    template_list = [{'id': temp.id, 'event_type': temp.event_type, 'template': temp.template} for temp in templates]
    return jsonify({'templates': template_list})
