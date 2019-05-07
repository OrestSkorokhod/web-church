from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    price = models.IntegerField()
    img = models.ImageField(upload_to='static', default='static/ikona.png')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.CharField(max_length=300, default='No text', db_index=True)
    user = models.CharField(max_length=100, default='Anon')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
