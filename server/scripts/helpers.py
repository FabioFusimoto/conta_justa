from ..models import Measurement

def getMeasurementCount():
    return len(Measurement.objects.all())
