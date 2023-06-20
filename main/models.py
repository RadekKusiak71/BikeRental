from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.username}'
    
class Bike(models.Model):
    bike_photo = models.ImageField(upload_to='bike-images')
    name = models.CharField(max_length=60)
    model = models.CharField(max_length=25)
    price = models.FloatField()
    is_avaiable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.is_avaiable}'
    
class RentOrder(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    session_key = models.CharField(max_length=255,null=True)
    firstname = models.CharField(max_length=60,null=True)
    lastname = models.CharField(max_length=60,null=True)
    email = models.EmailField(max_length=60,null=True)
    bike = models.ForeignKey(Bike,on_delete=models.CASCADE)
    rental_start_day = models.DateField(auto_now_add=True)
    rental_end_day = models.DateField()

    def __str__(self):
        if self.user:
            return f'{self.user} | {self.bike} rented to {self.rental_end_day}'
        else:
            return f'{self.session_key} | {self.bike} rented to {self.rental_end_day}'


