from django.urls import path
from .views import index,category,contact,single,detail

urlpatterns = [
    path('',index,name='index'),
    path('category',category,name='category'),
    path('contact',contact,name='contact'),
    path('single',single,name='single'),
    path('detail/<int:id>',detail,name='detail')
]


