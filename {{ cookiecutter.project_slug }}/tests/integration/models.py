from unittest import TestCase
from vcr_unittest import VCRTestCase
from rest_framework.test import APITestCase

from {{ cookiecutter.project_slug }}.models import (
    {{ cookiecutter.project_slug }},
    ES_{{ cookiecutter.project_slug }},
)


class Test_migration( APITestCase ):
    def test_index_should_exists( self ):
        index_exists = ES_{{ cookiecutter.project_slug }}.index.exists()
        self.assertTrue( index_exists )


class Test_model( VCRTestCase, APITestCase ):
    def _get_vcr_kwargs( self, **kw ):
        kw[ 'ignore_hosts' ] = [ 'localhost', 'waifus' ]
        return kw

    def test_should_work( self ):
        str( {{ cookiecutter.project_slug }} )
        str( ES_{{ cookiecutter.project_slug }} )
