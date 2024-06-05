from django.db import models


class mainNew(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.text


class professionNew(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class tablePrice(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='images/')
    price = models.TextField()

    def __str__(self):
        return self.name