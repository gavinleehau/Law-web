from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class article(models.Model):
  author =  models.CharField("Tên luật sư", default="", max_length=30)
  title = models.TextField("Tiêu đề", default="")
  date = models.DateTimeField("thời gian đăng")
  content = RichTextUploadingField("nội dung")
  image = models.ImageField(null=True)
  label = "Bài viết"

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-id']
    db_table = "article"