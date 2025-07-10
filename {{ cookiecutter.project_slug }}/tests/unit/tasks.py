from unittest import TestCase
from vcr_unittest import VCRTestCase
from rest_framework.test import APITestCase


from {{ cookiecutter.project_slug }}.tasks import debug_task


class Test_debug_task_with_vcr( VCRTestCase ):
    def _get_vcr_kwargs( self, **kw ):
        kw[ 'ignore_hosts' ] = [ 'localhost', 'waifus' ]
        return kw

    def test_should_work( self ):
        debug_task()
