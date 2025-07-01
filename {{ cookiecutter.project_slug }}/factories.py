import factory
from faker import Faker


class {{ cookiecutter.project_slug }}( factory.Factory ):
    field = factory.Faker( 'name' )

    class Meta:
        model = dict

