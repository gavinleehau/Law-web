from django.db import models
from ckeditor.fields import RichTextField
import datetime

# Create your models here.
class Questions(models.Model):
  question = models.CharField("Câu Hỏi: ",max_length=200, null=False)
  answer = RichTextField("Câu trả lời: ",default="",null=True)

  def __str__(self):
    return self.question

  class Meta:
    ordering = ['-id']
    db_table = "questions"

class social(models.Model):
  faceBook = models.CharField("Facebook", default="", max_length=1000)
  twitter = models.CharField("Facebook", default="", max_length=1000)
  instagram = models.CharField("Facebook", default="", max_length=1000)

  def __str__(self):
    return self.faceBook

  class Meta:
    db_table = "social"

class whyChooseUs(models.Model):
  title = models.CharField("Tiêu đề: ", default="", max_length=1000)
  detail = models.TextField("Chi tiết: ", default="")

  def __str__(self):
    return self.title

  class Meta:
    db_table = "why Choose Us"
          
        
        

