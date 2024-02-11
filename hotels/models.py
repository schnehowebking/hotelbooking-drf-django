from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.template.defaultfilters import slugify as default_slugify

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    address = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='hotels/images/')
    rooms = models.CharField(max_length=20)
    average_ratings = models.DecimalField(max_digits=12, decimal_places=2)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = default_slugify(self.name)
        super().save(*args, **kwargs)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel_rooms', on_delete=models.CASCADE)
    room_no = models.CharField(max_length=50)
    slug = models.SlugField()
    images = models.ImageField(upload_to='hotels/images/rooms/')
    description = models.TextField()
    bedrooms = models.IntegerField(validators=[MinValueValidator(1)])
    bathroom = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    child_facility = models.BooleanField(default=False)
    child_no = models.BooleanField(default=False)
    status = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = default_slugify(self.room_no)
        super().save(*args, **kwargs)
    

    def rent_room(self, customer):
        if self.status == 0:  # Assuming status 0 means room is available
            # Deduct the price_per_night from customer's balance
            customer.acc_balance -= self.hotel.price_per_night
            customer.save()
            self.status = 1  # Update status to indicate room is rented
            self.save()
            return True
        else:
            return False  # Room is not available

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name="reviews", on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Customer: {self.reviewer.first_name} - Hotel: {self.hotel.name}"