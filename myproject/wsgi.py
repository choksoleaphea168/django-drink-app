"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

app = application

if os.getenv("VERCEL"):
    try:
        from django.core.management import call_command
        call_command('migrate', interactive=False)
        
        from django.contrib.auth import get_user_model
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "chokveasna")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser '{username}' created successfully.")
    except Exception as e:
        print("Auto setup error:", e)


