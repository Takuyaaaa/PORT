from django.urls import path
from . import views

app_name = 'port'

urlpatterns =[
    path('',views.index,name='index'),
    path('<int:id>',views.detail,name='detail'),
    path('new',views.new, name='new'),
    path('create', views.create,name='create'),
    path('<int:id>/edit', views.edit,name='edit'),
    path('<int:id>/update', views.update,name='update'),
    path('<int:id>/delete', views.delete,name='delete'),
    path('<int:id>/confirm_delete', views.confirm_delete,name='confirm_delete'),
    path('<int:id>/des_edit', views.des_edit,name='des_edit'),
    path('<int:id>/des_update',views.des_update,name='des_update'),

]
