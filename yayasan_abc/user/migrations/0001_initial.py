from django.db import migrations
from django.contrib.auth.models import User

def create_users(apps, schema_editor):
    users = [
        ('andi', 'Andi', 'Setiawan', 'andi1234@example.com'),
        ('budi', 'Budi', 'Prasetyo', 'budi1234@example.com'),
        ('citra', 'Citra', 'Putri', 'citra1234@example.com'),
        ('dian', 'Dian', 'Susanti', 'dian1234@example.com'),
        ('eko', 'Eko', 'Wahyudi', 'eko1234@example.com'),
        ('fajar', 'Fajar', 'Hidayat', 'fajar1234@example.com'),
        ('gilang', 'Gilang', 'Sutrisno', 'gilang1234@example.com'),
        ('hendra', 'Hendra', 'Pramudya', 'hendra1234@example.com'),
        ('indah', 'Indah', 'Puspita', 'indah1234@example.com'),
        ('joko', 'Joko', 'Santoso', 'joko1234@example.com'),
    ]

    for username, first_name, last_name, email in users:
        User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password='password123')

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
