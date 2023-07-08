from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File

class TypeExercise(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}'
    
class Exercise(models.Model):
    type = models.ForeignKey(TypeExercise, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    others = models.CharField(max_length=255)
    instruction = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='exercises/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.type.slug}/{self.slug}'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        else:
            return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
            
    def make_thumbnail(self, image, size = (300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

