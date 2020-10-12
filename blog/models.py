from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200,
    choices = [
    ("NEJM","NEJM"),("JACC","JACC"),("Circulation","Circulation"),
    ],
    null=True
    )
    published_year = models.CharField(
    max_length = 50,
    choices = [("2016","2016年"),("2017","2017年"),("2018","2018年"),
    ("2019","2019年"),("2020","2020年"),
    ],
    null=True
    )
    text = models.TextField()
    category = models.CharField(
    max_length = 50,
    choices = [
    ("TAVR","TAVR"),("CAD","CAD"),("Economic","Economic"),
    ],
    null=True
    )
    Tag = models.CharField(max_length = 50,blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
