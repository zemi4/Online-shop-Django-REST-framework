from celery import task, shared_task
from django.core.mail import send_mail
from .models import Order
from myshop.celery import app


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    print(mail_sent)
    return mail_sent

# from celery import shared_task, Celery
# import os
#
# # os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
# # app = Celery('myshop')
#
#
# @shared_task
# def adding_task(x, y):
#     return x + y

# import logging
#
# from django.urls import reverse
# from django.core.mail import send_mail
# from django.contrib.auth import get_user_model
# from myshop.celery import app
#
#
# @app.task
# def send_verification_email(user_id):
#     UserModel = get_user_model()
#     try:
#         user = UserModel.objects.get(pk=user_id)
#         send_mail(
#             'Verify your QuickPublisher account',
#             'Follow this link to verify your account: '
#             'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
#             'from@quickpublisher.dev',
#             [user.email],
#             fail_silently=False,
#         )
#     except UserModel.DoesNotExist:
#         logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
