from celery import shared_task

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string



@shared_task
def send_confirmation_email(customer_name, customer_email):

	template = render_to_string('store/confirmation_email.html', {'name': customer_name})

	email = EmailMessage(
		'Thanks for purchasing products from our website!',
		template,
		settings.EMAIL_HOST_USER,
		[customer_email],
		)

	email.fail_silently=False
	email.send()

	return None