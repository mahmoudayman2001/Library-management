from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name



class BooK(models.Model):

    status = [
        ('availble', 'availble'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]




    title = models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    photo_book = models.ImageField(upload_to='phtos', null=True, blank=True)
    photo_auther = models.ImageField(upload_to='phtos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits= 4 , decimal_places= 2, null=True, blank=True)
    retal_price = models.DecimalField(max_digits= 4 , decimal_places= 2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    total_retal =  models.DecimalField(max_digits= 4 , decimal_places= 2, null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    status = models.CharField(max_length=30, choices=status, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


