from django.urls import path

from .views import GetTestTable

app_name = 'Core'
urlpatterns=[
    path('test', GetTestTable.as_view())
]