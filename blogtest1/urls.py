from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    #会匹配/list/1/show     /list/2/show
    path('<int:post_id>/show',views.show,name='show'),
]