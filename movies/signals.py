from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import mail_managers, send_mail
from .models import Movie, Review
from django.conf import settings
from django.contrib.auth.models import User

# send mail to managers when create or update movie
@receiver(post_save, sender=Movie)
def movie_add_notify(sender, instance, created, **kwargs):
    if getattr(instance, '_skip_notification', False):
        return  # ignore if flag true
    if created:
        subject=f'Добавление фильма {instance.name}'
    else:
        subject = f'Внесение изменений в {instance.name}'
    send_mail(
        subject=subject,
        message=instance.description,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email for name, email in settings.MANAGERS],
    )

@receiver(post_save, sender=Review)
def review_add_notify(sender, instance, created, **kwargs):
    subs = instance.movie.subscribers.all()
    emails = list(subs.values_list('email', flat=True))
    subject = f'Добавление отзыва к фильму {instance.movie.name}'
    send_mail(
        subject=subject,
        message=instance.title,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=emails,
    )