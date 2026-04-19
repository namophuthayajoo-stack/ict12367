from django.urls import path
from myapp import views
urlpatterns =[
    path('',views.index),
    path('about',views.about),
    path('form/',views.form, name='form'),
    path('edit/<int:person_id>/',views.edit, name='edit'),
    path('delete/<int:person_id>/',views.delete, name='delete'),
]