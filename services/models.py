from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Services(models.Model):
    title = models.TextField("Tiêu đề", default="")
    content = RichTextField("nội dung")
    label = "Dịch vụ"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        db_table = "services"