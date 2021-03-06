from django.contrib import admin
from app_account.models import UserProfile, UserAddress


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'national_code', 'image_tag']


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'ostan', 'city', 'selected']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
