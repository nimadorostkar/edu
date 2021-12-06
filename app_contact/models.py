from django.db import models
from django.db.models.base import Model







#------------------------------------------------------------------------------
class Contact(models.Model):
    name = models.CharField(max_length=80, verbose_name="نام")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    subject = models.CharField(max_length=200, verbose_name="موضوع")
    body = models.TextField(verbose_name="متن پیام")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
      verbose_name = "تماس"
      verbose_name_plural = "تماس ها"

    def __str__(self):
        return str(self.name)






#------------------------------------------------------------------------------
class Newsletter(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
      verbose_name = "خبرنامه"
      verbose_name_plural = " خبرنامه  ها"

    def __str__(self):
        return str(self.email)
