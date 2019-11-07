from django.db import models
from .utils import generate_random_string

class UrlModel(models.Model):
    original_url = models.URLField(verbose_name='Provide url here:')
    shortened_url = models.URLField()
    url_slug = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    # On submit create shortened slug and full redirect url
    def save(self, *args, **kwargs):
        new_slug = generate_random_string()
        new_url = 'http://localhost:8000/'+new_slug
        
        self.shortened_url = new_url
        self.url_slug = new_slug
        super(UrlModel, self).save(*args, **kwargs)
