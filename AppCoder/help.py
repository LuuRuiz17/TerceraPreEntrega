import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nombre_de_tu_proyecto.settings')
import django
django.setup()

from django.contrib.auth.models import User
user = User.objects.get(username='tu_nombre_de_usuario')
print(user.username)
print(user.email)
