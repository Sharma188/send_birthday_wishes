from datetime import datetime

from flask_celery import Celery
from app import app
from models import Employee, Event, EmailTemplate

celery = Celery(app)


def send_email(to_email, subject, content):
    print(f"Sending email to {to_email} - Subject: {subject}, Content: {content}")


@celery.task
def send_event_emails():
    today = datetime.now().date()
    events_today = Event.query.filter_by(event_date=today).all()

    for event in events_today:
        template = EmailTemplate.query.filter_by(event_type=event.event_type).first()
        if template:
            employees = Employee.query.all()

            for emp in employees:
                send_email(emp.email, "Event Reminder",
                           template.template.format(name=emp.name, event_type=event.event_type))
