from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='home'),
    path('about/',views.about, name='about'),
    path('login/',views.login, name='login'),
    path('Add/',views.Add, name='Add'),
    path('Modify/',views.Modify, name='Modify'),
    path('attendancesheet/',views.attendancesheet, name='attendancesheet'),

]