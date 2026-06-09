import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpl_project.settings')
django.setup()

from django.contrib.auth.models import User

user = User.objects.get(username='admin')
user.set_password('123456789')
user.save()

print("Password changed successfully!")
