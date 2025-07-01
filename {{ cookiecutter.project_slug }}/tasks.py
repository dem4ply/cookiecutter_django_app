from celery.utils.log import get_task_logger
from celery.schedules import crontab


from celery.utils.log import get_task_logger
from celery.schedules import crontab

from chibi_datahouse.tasks_class import Task_base
from chibi_datahouse.app_celery import chibi_datahouse_task as celery_task
from chibi_requests import Chibi_url
from danbooru.scrapper import danbooru, Danbooru_post, Danbooru
from danbooru.serializers import Post as Post_serializer
from danbooru.models import Post as Post_model

from chibi_site import Chibi_site


logger = get_task_logger( '{{ cookiecutter.project_slug }}.task.danbooru' )


@celery_task.task( bind=True, base=Task_base, ignore_result=True )
def debug_task( self, *args, **kw ):
    logger.debug(
        "execute task for debug in {{ cookiecutter.project_slug }}",
        extra={ 'params': { 'args': args, 'kargs': kw } } )


@celery_task.task(
    bind=True, base=Task_base, ignore_results=True, max_retries=3,
    rate_limit='30/m' )
def example_task( self, *args, **kw ):
    logger.info(
        "execute task for debug in {{ cookiecutter.project_slug }}",
    )


@celery_task.on_after_configure.connect
def setup_periodic_tasks( sender, **kw ):
    sender.add_periodic_task(
        crontab( hour=12, minute=0 ),
        example_task.s(),
    )
