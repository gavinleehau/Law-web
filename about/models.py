from django.db import models
from ckeditor.fields import RichTextField
import datetime

# Create your models here.
class info(models.Model):
  firstName = models.CharField("Họ", default="", max_length=50,null=False )
  lastName = models.CharField("Tên", default="",max_length=50,null=False)
  position = models.CharField("Chức vụ", default="",max_length=20,null=False)
  phoneNumber = models.CharField("Số điện thoại", default="",max_length=11,null=True)
  email = models.CharField("email", default="", max_length=100,null=True)
  address = models.CharField("Địa chỉ", default="",max_length=200,null=True)
  birth_date = models.DateField("Ngày sinh",null=True)
  descriptions = RichTextField("Giới thiệu",default="",null=True)
  avata = models.ImageField("Ảnh đại diện", null=True)
  
  
  def __str__(self):
    displayName = self.firstName + ' ' + self.lastName
    return displayName

  def get_age(self):
    age = datetime.date.today() - self.birth_date
    return int((age).days / 365.25)

class local_info(info):
  class meta:
    db_table = "info"

class member(info):
  faceBook = models.CharField("Facebook", default="", max_length=1000)
  twitter = models.CharField("Facebook", default="", max_length=1000)
  instagram = models.CharField("Facebook", default="", max_length=1000)
  class meta:
    odering = ['-id']
    db_table = "member"

class history(models.Model):
  title = models.CharField("Tiêu đề", default="", max_length=100)
  date = models.DateField("Thời điểm")
  event = models.TextField("Sự kiện", default="",max_length=100000)

  def __str__(self):
      return self.title

  class meta:
    odering = ['-id']
    db_table = "history"
          
        

        