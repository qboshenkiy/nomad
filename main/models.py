from django.db import models


class mainNew(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class professionNew(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class tablePrice(models.Model):
    icon = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name