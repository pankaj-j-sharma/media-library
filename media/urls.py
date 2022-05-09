from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='media_detail'),
    path('update/<int:id>', views.update, name='media_update'),
    path('delete/<int:id>', views.delete, name='media_delete'),
    path('create', views.create, name='create_new'),

    path('categories', views.categories, name='category_list'),
    path('addcategory', views.add_category, name='add_category'),

]
