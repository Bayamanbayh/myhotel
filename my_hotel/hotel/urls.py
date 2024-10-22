from django.urls import path
from .views import *

urlpatterns = [
    path('', BookingListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', BookingDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('users/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_detail'),

    path('hotel/', HotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('hotel/<int:pk>/', BookingDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='hotel_detail'),

    path('photos_hotel/', ImageHotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='photoshotel_list'),
    path('photos_hotel/<int:pk>/', ImageHotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='photoshotel_detail'),

    path('room/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='room_detail'),

    path('photos_room/', ImageRoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='photosroom_list'),
    path('photos_room/<int:pk>/', ImageRoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='photosroom_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),

    path('photos/', ImageBookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='photos_list'),
    path('photos/<int:pk>/', ImageBookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='photos_detail'),

    path('cart/', FavoriteViewSet.as_view({'get': 'retrieve'}), name='cart_detail'),
    path('cart_items/', FavoriteHotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_item_list'),
    path('cart_items/<int:pk>/', FavoriteHotelViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]