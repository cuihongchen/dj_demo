from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    objects = models.Manager() #使模型实例有objects属性
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # on_delete是新版django参数属性，指一对多的关系
    owner = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.text

class Entry(models.Model):
    objects = models.Manager()
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50]+"....."