from rq_scheduler import Scheduler
from redis import Redis
import django_rq
import datetime
from datetime import datetime

from server.constants import ADD_MEASURE_EVENT

from server.connectors.measurement_scheduler import measurement_scheduler

from django_rq.management.commands import rqscheduler


def printAlgo():
    print("Esta funcionando: ")
    print(datetime.now())


# def ready():
#     scheduler = django_rq.get_scheduler("default", interval=15)
#
#     scheduler.schedule(
#         scheduled_time=datetime.utcnow(),  # Time for first execution, in UTC timezone
#         func=printAlgo,  # Function to be queued
#         args=[],  # Arguments passed into function when executed
#         kwargs={},  # Keyword arguments passed into function when executed
#         interval=30,  # Time before the function is called again, in seconds
#         repeat=None,  # Repeat this number of times (None means repeat forever)
#     )
#     scheduler.run()
#
#
# ready()

scheduler = django_rq.get_scheduler("default", interval=15)

def clear_scheduled_jobs():
    # Delete any existing jobs in the scheduler when the app starts up
    for job in scheduler.get_jobs():
        job.delete()

def register_scheduled_jobs():
    # do your scheduling here
    scheduler.schedule(
        scheduled_time=datetime.utcnow(),  # Time for first execution, in UTC timezone
        func=printAlgo,  # Function to be queued
        args=[],  # Arguments passed into function when executed
        kwargs={},  # Keyword arguments passed into function when executed
        interval=30,  # Time before the function is called again, in seconds
        repeat=None,  # Repeat this number of times (None means repeat forever)
    )


class Command(rqscheduler.Command):
    def handle(self, *args, **kwargs):
        # This is necessary to prevent dupes
        clear_scheduled_jobs()
        register_scheduled_jobs()
        super(Command, self).handle(*args, **kwargs)
