from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.TextField(max_length=120)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    menssage=models.TextField(max_length=300)

    def __str__(self):
        return '{}'.format(self.name)
    
    def save(self):
        super(Contact, self).save()