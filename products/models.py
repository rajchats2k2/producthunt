from django.db import models
from django.contrib.auth.models import User
from datetimepicker.widgets import DateTimePicker

# Create your models here.


# product class

# title
# pub_date
# image
# icon
# body
# pub_date_pretty

# url
# votes_total


# hunter

class Product(models.Model):
    title= models.CharField(max_length=255)
    #pub_date= models.DateTimeField(('Creation date'), help_text=('Date of the creation'), auto_now_add=True, blank=True)
    pub_date= models.DateTimeField()
    body= models.TextField()
    url= models.URLField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/', null=True)
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
