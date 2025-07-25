from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='kasimov/videos/')

    def __str__(self):
        return self.video.name
    

class ServiceCategory(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='kasimov/service_category/image/')
    video =  models.FileField(upload_to='kasimov/service_category/video/')

    def __str__(self):
        return f'{self.id} - {self.title}'


class Service(models.Model):
    file = models.FileField(upload_to='kasimov/service/image/', null=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.file.name}'
    

class Gallery(models.Model):
    image = models.ImageField(upload_to='kasimov/gallery/')

    def __str__(self):
        return self.image.name
    

class Partner(models.Model):
    icon = models.ImageField(upload_to='kasimov/partner/')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.link if self.link else self.icon.name
    

class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='kasimov/about_us/')

    def __str__(self):
        return f'{self.id} - {self.title_uz}'
    

class Team(models.Model):
    image = models.ImageField(upload_to='kasimov/team/')
    full_name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.id} - {self.full_name}'
