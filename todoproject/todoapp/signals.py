from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Task


@receiver(post_save, sender=Task)
def task_created(sender, instance, created, **kwargs):
    if created:
        print(f"Task Created = {instance.title}")


@receiver(pre_delete, sender=Task)
def task_deleted(sender, instance, **kwargs):
    print(f"Task Deleted: {instance.title}")
