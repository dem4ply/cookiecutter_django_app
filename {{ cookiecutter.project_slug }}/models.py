from django.db import models
from chibi_django.models import Chibi_model, ES_document
from django.utils.translation import gettext_lazy as _
from elasticsearcch_dsl import field


class {{ cookiecutter.project_slug }}( Chibi_model ):
    create_at = models.DateTimeField(
        _( "creation date" ), auto_now_add=True )
    update_at = models.DateTimeField(
        _( "last update date" ), auto_now=True )


class ES_{{ cookiecutter.project_slug }}( ES_document ):
    name = field.Text(
        analyzer=name, multi=True,
        fields={
            'space': field.Text( analyzer=name_space, multi=True )
            'keyword': field.Text( multi=True )
        }, )
    url = field.keyword()
    create_at = field.Date
    update_at = field.date

    class Index:
        name = build_index_name( '{{ cookiecutter.project_slug }}' )
        settings = { 'number_of_shards': 2, 'number_of_replicas': 1 }
