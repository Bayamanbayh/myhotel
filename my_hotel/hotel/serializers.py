from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'password', 'first_name', 'last_name',
                  'age', 'date_registered', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class ImageHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageHotel
        fields = '__all__'

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ImageRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageRoom
        fields = '__all__'

class BookingListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'hotel', 'check_in_date', 'check_out_date', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class BookingDetailSerializers(serializers.ModelSerializer):
    genre = HotelSerializers()
    ratings = RatingSerializers(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    year = serializers.DateField(format='%d-%m-%Y')
    owner = ProfileSerializers()

    class Meta:
        model = Booking
        fields = '__all__'

    def get_average_rating(self, obj):
        return obj.get_average_rating()

class ImageBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageBooking
        fields = '__all__'

class FavoriteHotelSerializer(serializers.ModelSerializer):
    booking = BookingListSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all(), write_only=True, source='product')

    class Meta:
        model = FavoriteHotel
        fields = ['id', 'booking', 'booking_id', 'quantity', 'get_total_price']

class FavoriteSerializers(serializers.ModelSerializer):
    items = FavoriteHotelSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'items', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()


