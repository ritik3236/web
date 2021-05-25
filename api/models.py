from django.db import models

# Create your models here.


class QuotesApi(models.Model):
    author = models.CharField(max_length=20, default='Anonymous')
    author_img = models.ImageField(upload_to='quote/', blank=True, null=True)
    quote_type = models.CharField(max_length=20, blank=True)
    source = models.CharField(max_length=20, blank=True, default='Reddit')
    quote = models.TextField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    @property
    def sort_quote(self):
        return ' '.join(self.quote.split()[:21])

