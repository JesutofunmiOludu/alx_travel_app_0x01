from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Listing, Review, Booking
from .serializers import ListingSerializer, ReviewSerializer, BookingSerializer
from rest_framework import viewsets


# Create your views here.


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
"""
@api_view(['GET'])
def listing_list(request):
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def listing_detail(request, pk):
    try:
        listing = Listing.objects.get(property_id=pk)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ListingSerializer(listing)
    return Response(serializer.data)
@api_view(['POST'])
def listing_create(request):
    serializer = ListingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def listing_update(request, pk):
        try:
        listing = Listing.objects.get(property_id=pk)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def listing_delete(request, pk):
    try:
        listing = Listing.objects.get(property_id=pk)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    listing.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    """