from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class news(models.Model):
  author =  models.CharField("Tên Người đăng: ", default="", max_length=30)
  title = models.CharField("Tiêu đề", default="", max_length=200)
  date = models.DateTimeField("thời gian đăng")
  demo = models.TextField("Bản giới thiệu", default="")
  content = RichTextField("nội dung")
  link = models.CharField("Link nguồn", max_length=100000)
  image = models.ImageField(null=True)
  label = "Tin tức"

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-id']
    db_table = "news"