from django.contrib import admin

# Register your models here.
# user_profile/admin.py
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    # Указываем, какие поля будут отображаться в списке объектов
    list_display = ('user', 'phone_number', 'image')  # Поля, которые будут отображаться в списке
    # Добавляем фильтрацию по пользователю
    search_fields = ('user__username', 'phone_number')  # Поля, по которым можно искать
    # Добавляем возможность фильтрации по пользователю
    list_filter = ('user',)
    # Указываем, что эти поля должны редактироваться в форме
    fields = ('user', 'phone_number', 'image')

# Регистрируем модель UserProfile с кастомным админом
admin.site.register(UserProfile, UserProfileAdmin)
