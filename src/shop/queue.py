from shop.models import Queue

class UniqueQueue:

    def add(self, unit):
        if not Queue.objects.filter(value = unit).exists():
            Queue.objects.create(value = unit)

    def last(self):
        if Queue.objects.exists():
            return Queue.objects.order_by("id").last().value
        return None

    def length(self):
        return Queue.objects.count()