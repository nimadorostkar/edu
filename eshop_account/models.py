from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save





def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_id = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_id}-{instance.user}{ext}"
    return f"users/image/{final_name}"






class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام', related_name='profile')
    phone = models.CharField(blank=True, max_length=20, verbose_name='تلفن')
    national_code = models.CharField(blank=True, max_length=20, verbose_name='کدملی', default='_')
    image = models.ImageField(blank=True, null=True, upload_to=upload_image_path, verbose_name='تصویر')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ( ' + self.user.username + ' ) '

    user_name.short_description = 'نام کاربری'

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'تصویر'







class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    full_name = models.CharField(blank=True, max_length=60, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(blank=True, max_length=20, verbose_name='تلفن')
    ostan = models.CharField(blank=True, max_length=20, verbose_name='استان')
    city = models.CharField(blank=True, max_length=20, verbose_name='شهر')
    address = models.CharField(blank=True, max_length=150, verbose_name='آدرس پستی')
    post_code = models.IntegerField(blank=True, verbose_name='کد پستی', null=True)
    selected = models.BooleanField(default=False, verbose_name='آدرس منتخب')

    def user_name(self):
        return self.full_name + ' ( ' + self.user.username + ' ) '

    class Meta:
        verbose_name = 'آدرس کاربر'
        verbose_name_plural = 'آدرس کاربران'

    def __str__(self):
        return self.user.username











# End
