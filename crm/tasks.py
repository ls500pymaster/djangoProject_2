from celery import task
from django.core.mail import send_mail
from .models import Book

@task
def order_created(name):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Book.objects.get(name=name)
    subject = 'Order nr. {}'.format(name)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@crm.com',
                          [order.email])
    return mail_sent