from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    mobile_number = models.IntegerField()
    email = models.EmailField()
    logo = models.ImageField(upload_to="images")
    facebook = models.CharField(max_length=250, null=True, blank=True)
    twitter = models.CharField(max_length=250, null=True, blank=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    youtube = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural="Company"




class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateField()
    organiser = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to = "images")
    

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Events"

class Image(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.ImageField(
        null=True, upload_to='events', default='img_default.jpg')
    date_created = models.DateTimeField(auto_now=True)

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "About"


class History(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "History"

class Front_Persons(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Front Persons"
    

class Writer(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    father = models.CharField(max_length=200)
    mother = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "images")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Writer"