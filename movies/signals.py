from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import mail_managers, send_mail
from .models import Movie
from django.conf import settings

@receiver(post_save, sender=Movie)
def movie_add_notify(sender, instance, created, **kwargs):
    subject=f'Добавление фильма {instance.name}'
    # mail_managers(
    #     subject=subject,
    #     message=instance.description,
    # )
    send_mail(
        subject=subject,
        message=instance.description,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email for name, email in settings.MANAGERS],
    )
