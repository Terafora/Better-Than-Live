from django.db import models
from django.contrib.auth.models import User
from .event import Event


class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_types')
    category = models.CharField(max_length=50)
    price_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=1.0)

    def __str__(self):
        return f"{self.category} for {self.event.title}"