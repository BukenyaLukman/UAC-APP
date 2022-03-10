from django.contrib import admin

# Register your models here.

from .models import Register,Login


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username','age','FirstName','SurName','Hiv_status','phone_number','email','password')
    list_filter = ('username','age','FirstName','SurName','Hiv_status','phone_number','email','password')
    search_fields = ('username','age','FirstName','SurName','Hiv_status','phone_number','email','password')


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username','password')
    list_filter = ('username','password')
    search_fields = ('username','password')

