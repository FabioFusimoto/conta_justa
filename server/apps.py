from django.apps import AppConfig

from rq_scheduler import Scheduler
import django_rq

from datetime import datetime

from server.constants import ADD_MEASURE_EVENT

from server.measurement_scheduler import measurement_scheduler


class ServerConfig(AppConfig):
    name = 'server'

    def ready(self):
        scheduler = django_rq.get_scheduler('default')

        # Delete any existing jobs in the scheduler when the app starts up
        for job in Scheduler.get_jobs():
            job.delete()

        scheduler.schedule(
            scheduled_time=datetime.utcnow(),  # Time for first execution, in UTC timezone
            func=measurement_scheduler,  # Function to be queued
            args=[ADD_MEASURE_EVENT],  # Arguments passed into function when executed
            kwargs={},  # Keyword arguments passed into function when executed
            interval=10,  # Time before the function is called again, in seconds
            repeat=None,  # Repeat this number of times (None means repeat forever)
            meta={}  # Arbitrary pickleable data on the job itself
        )