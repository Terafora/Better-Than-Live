from django.urls import path
from .views import EventListAPI, TicketTypeAPI

urlpatterns = [
    path('api/events/', EventListAPI.as_view(), name='event_list_api'),
    path('api/events/<int:event_id>/tickets/', TicketTypeAPI.as_view(), name='ticket_type_api'),
]
