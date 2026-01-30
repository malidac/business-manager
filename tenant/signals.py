from django.db.models.signals import post_save
from django.dispatch import receiver
from tenant.models import Company


@receiver(post_save, sender=Company)
def set_owner_company(sender, instance, created, **kwargs):
    if created and instance.owner.company is None:
        instance.owner.company = instance
        instance.owner.save()
