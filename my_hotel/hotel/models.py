from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], null=True, blank=True)
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    STATUS_CHOICES = (
        ('vip', 'vip'),
        ('normal', 'normal')
    )

class Hotel(models.Model):
    name_hotel = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)

    def str(self):
        return f'{self.name_hotel} - {self.country}'


class ImageHotel(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_images/')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.SmallIntegerField(default=0)
    capacity = models.PositiveIntegerField(default=0)
    price_per_night = models.PositiveIntegerField()

    def str(self):
        return f'{self.room_number}'


class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_images/')


class Booking(models.Model):
    user = models.CharField(max_length=32)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ('Бронь', 'Бронь'),
        ('Свободный', 'Свободный'),
        ('Занят', 'Занят')
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0

class ImageBooking(models.Model):
    video = models.FileField(upload_to='movie_languages/')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='movie_language')

    def __str__(self):
        return f'{self.booking}'

class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], verbose_name='рейтинг')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

class Favorite(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

class FavoriteHotel(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Booking, on_delete=models.CASCADE)