import os
from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "brewery_project.settings")
apps.populate(settings.INSTALLED_APPS)

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware

from api_app.endpoints import api_router


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")
    app.mount("", WSGIMiddleware(get_wsgi_application()))

    return app


application = get_application()
