from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    for user in User.objects.all():
        if not hasattr(user, 'customer'):
            Customer.objects.create(user=user)
            print(f"Customer created for user: {user.username}")
