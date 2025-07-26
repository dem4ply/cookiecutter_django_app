from django.apps import AppConfig


class {{ cookiecutter.project_slug | capitalize }}_config( AppConfig ):
    name = '{{ cookiecutter.project_slug }}'
