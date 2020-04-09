from django.db import models

# Create your models here.


class Laptop(models.Model):
    new = models.BooleanField(default=False)
    name = models.TextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name


class Phones(models.Model):
    new = models.BooleanField(default=False)
    name = models.TextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name


class Computers(models.Model):
    model = models.CharField(max_length=100)
    amount = models.IntegerField()
    spec = models.TextField()
    image = models.ImageField(upload_to='image')
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.model


class Iphones(models.Model):
    model = models.CharField(max_length=100)
    amount = models.IntegerField()
    spec = models.TextField()
    image = models.ImageField(upload_to='image')
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.model


class Quiz(models.Model):
    image = models.ImageField(upload_to='image')
    text = models.TextField()

    def __str__(self):
        return self.text

