from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import mail_managers, send_mail
from .models import Movie
from django.conf import settings

# send mail to managers when create or update movie
@receiver(post_save, sender=Movie)
def movie_add_notify(sender, instance, created, **kwargs):
    if getattr(instance, '_skip_notification', False):
        return  # игнорируем это сохранение
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
