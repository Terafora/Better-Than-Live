from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, TicketType
from .serializers import EventSerializer, TicketTypeSerializer

class EventListAPI(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class TicketTypeAPI(APIView):
    def get(self, request, event_id):
        ticket_types = TicketType.objects.filter(event_id=event_id)
        serializer = TicketTypeSerializer(ticket_types, many=True)
        return Response(serializer.data)
