from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=155)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Food(models.Model):
    image = models.ImageField(upload_to='food/')
    title = models.CharField(max_length=55)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey('app.Category', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

    def __str__(self):
        return f"{self.image}, {self.title}, \n" \
               f"{self.description}, ${self.price}"

class Chef(models.Model):
    image = models.ImageField(upload_to='chef/')
    name = models.CharField(max_length=55)
    job = models.CharField(max_length=55)
    text = models.TextField()

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'

    def __str__(self):
        return f"{self.image}, {self.name}\n" \
               f"{self.job}, {self.text}"


# class BookTable(models.Model):
#     name = models.CharField(max_length=155)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=13)
#     data = models.DateField()
#     time = models.TimeField()
#     people = models.IntegerField(default=1)
#     message = models.TextField()
#
#     def __str__(self):
#         return self.name

class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name