from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
import datetime
import re
from django.utils.dateparse import parse_date, parse_datetime, parse_time
from time import strptime
from datetime import date

class TaskItem(models.Model):
    taskn = models.CharField(max_length = 400)
    due_date = models.CharField(max_length = 20, default='')
    due_time = models.CharField(max_length = 20, default='None')
    information = models.CharField(max_length = 4000, default = 'Additional information')
    usern = models.ForeignKey(User)
    created_date = models.DateTimeField('date created', default=timezone.now, editable = False)
    created_time = models.TimeField('time created', auto_now_add = True, editable = False)

    def __unicode__(self):
        return self.taskn 
        # + " at " + str(self.created_time)

