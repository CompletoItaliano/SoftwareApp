import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoftwareApp.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import call_command

print("👉 Ejecutando migraciones...")
call_command('migrate')

print("👉 Creando superusuario (si no existe)...")
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✅ Usuario admin creado: usuario=admin, contraseña=admin123")
else:
    print("⚠️ El usuario admin ya existe.")
