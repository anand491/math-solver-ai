from flask import Flask

app = Flask(name)

@app.route('/') def hello_world(): return 'Hello, World!'

if name == 'main': app.run() import os from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

application = get_wsgi_application() gunicorn app:app gunicorn your_project_name.wsgi:application sudo apt install nginxserver { listen 80; server_name yourdomain.com;

location / {
    proxy_pass http://127.0.0.1:8000;  # This should match your Gunicorn port
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

} sudo systemctl daemon-reload sudo systemctl start gunicorn sudo systemctl enable gunicorn

