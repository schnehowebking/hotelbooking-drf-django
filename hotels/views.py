from rest_framework import viewsets, generics
from .models import Hotel, Review
from .serializers import HotelSerializer, RoomSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get(self.lookup_field)
        return queryset.filter(slug=slug)
    

    @action(detail=True, methods=['post'])
    def rent_room(self, request, slug=None):
        hotel = self.get_object()
        room_id = request.data.get('room_id')
        room = hotel.hotel_rooms.filter(id=room_id).first()
        if room:
            customer = request.user.customer
            if room.rent_room(customer):
                return Response({'success': 'Room rented successfully.'})
            else:
                return Response({'error': 'Room is not available.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Room not found.'}, status=status.HTTP_404_NOT_FOUND)

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer