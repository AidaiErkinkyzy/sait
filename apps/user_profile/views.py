# user_profile/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class UserProfileView(TemplateView):
    template_name = 'pages/user_profile.html'  # Убедитесь, что путь правильный