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


class FileUpload(models.Model):
    file_type_choice = [('ques', 'Question Paper'),
                        ('notes', 'Notes'),
                        ('solution', 'Solution')]

    name = models.CharField(max_length=30,)
    email = models.EmailField(max_length=50, blank=True)
    type = models.CharField(
        max_length=10, choices=file_type_choice, default='ques')
    document = models.FileField(upload_to='userUploaded/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        try:
            x = self.document.name.split('/')
            y = self.name.split(' ')
            return f"{y[0]}, {x[1]}"
        except :
            return self.name
