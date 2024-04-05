
from django.urls import path
from .views.web import views
from .views.rest import views as rest

urlpatterns = [
    # site urls
    path('', views.SingUpView.as_view(), name='singup'),

    # api urls
    path('api/login/', rest.LoginRest.as_view(), name='rest_login'),
]
