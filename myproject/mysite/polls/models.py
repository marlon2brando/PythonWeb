from django.db import models
from django.utils import timezone

import datetime
# Create your models here.

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Question(models.Model):
    choice = models.ManyToManyField(Choice,blank=True,null=True)
    # choice = models.ManyToManyField(Choice)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def was_published_recently(self):
        now = timezone.now()    
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field= 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text
    
class SurveyPage(models.Model):
    question = models.ManyToManyField(Question,blank=True, null=True)
    title = models.CharField(max_length=200)
    # answer_person = models.ForeignKey(User)



