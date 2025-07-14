from celery.utils.log import get_task_logger
from celery.schedules import crontab

from {{ cookiecutter.django_project }}.tasks_class import Task_base
from {{ cookiecutter.django_project }}.app_celery import {{ cookiecutter.django_project }}_task as celery_task


logger = get_task_logger( '{{ cookiecutter.project_slug }}.task' )


@celery_task.task( bind=True, base=Task_base, ignore_result=True )
def debug_task( self, *args, **kw ):
    logger.debug(
        "execute task for debug in {{ cookiecutter.project_slug }}",
        extra={ 'params': { 'args': args, 'kargs': kw } } )


@celery_task.task(
    bind=True, base=Task_base, ignore_result=True, max_retries=3,
    rate_limit='30/m' )
def example_task( self, *args, **kw ):
    logger.info(
        "execute task for example in {{ cookiecutter.project_slug }}",
    )


@celery_task.on_after_finalize.connect
def setup_periodic_tasks( sender, **kw ):
    sender.add_periodic_task(
        crontab( minute='*/5' ),
        example_task.s(),
    )
