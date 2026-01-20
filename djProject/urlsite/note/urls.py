from django.urls import path, include
from .views import *

urlpatterns = [
   path('', note_page),
   path('form/', form),
   path('thanks/', thanks, name="thanks_page"),
]
