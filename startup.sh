#!/bin/bash
cd /home/site/wwwroot
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn django_azure_storage.wsgi --timeout 600
```

Then in **Azure Portal → Startup Command**:
```
bash /home/site/wwwroot/startup.sh