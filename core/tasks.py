import datetime

from django.core.mail import send_mass_mail, BadHeaderError
from .models import Task
from datetime import timedelta
from templated_mail.mail import BaseEmailMessage
from celery import shared_task


@shared_task()
def check_deadlines():
    qs = Task.objects.filter(status='p').filter(expire_at=(datetime.date.today()) + timedelta(days=1)) \
        .select_related('board__workspace__owner').all()

    print("processing .")

    for item in qs:
        user_email = item.board.workspace.owner.email
        title_task = item.description
        send_reminder_email(title_task, user_email)


def send_reminder_email(title, user_email):
    subject = 'Reminder: Deadline of your Task is around the corner. '
    body = f'This is a reminder for ({title}) Task.'
    from_email = 'Trenna@gmail.com'
    to_email = [user_email]

    try:
        # send_mass_mail(subject, body, from_email, to_email)
        m = BaseEmailMessage(template_name='email/reminder.html', context={'subject': subject, 'message': body})
        m.send(to_email)
    except BadHeaderError:
        pass
