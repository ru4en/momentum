from django.db import models
# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class notes(models.Model):
    id = models.AutoField(db_column='note_id', primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class documents(models.Model):
    id = models.AutoField(db_column='documents_id', primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    expiry_date = models.DateField()

    def __str__(self):
        return self.title


