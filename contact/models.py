from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField("Họ tên: ", max_length=50, null=True)
    phone = models.CharField("Số điện thoại: ", max_length=12, null=True)
    email = models.CharField("Email: ", max_length=100, null=True)
    subject = models.CharField("Tiêu đề", max_length=100, null=True)
    message = models.TextField("Nội dung", null=True)

    class meta:
        odering = ['-id']
        db_table = "contact"

    def __str__(self):
      	return self.email


        