from django.urls import path
from .views import *

urlpatterns=[
    path("hv/",homeview),
    path("av/",addview),
    path("sv/",showview),
    path("dv/<int:x>/",deleteview),
    path("uv/<int:pk>/",updateview)

]