from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

app_name = 'hotels'
router.register(app_name, views.HotelViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('hotel/<slug:slug>/', views.HotelDetail.as_view({'get': 'retrieve'}), name='hotel-detail'),
    path('reviews/', views.ReviewListCreate.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('pre-book-request/', views.PreBookRequestCreateAPIView.as_view(), name='pre_book_request_create'),
    path('contact-us/', views.ContactUsCreateAPIView.as_view(), name='contact_us_create'),
    
]