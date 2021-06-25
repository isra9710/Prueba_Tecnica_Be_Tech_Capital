from django.urls import path
from . import views
app_name = 'users_crud'
urlpatterns = [
    path('index', views.UserListView.as_view(), name='index'),
    path('search', views.UserSearchListView.as_view(), name='search'),
    path('update/<int:pk>', views.update_user, name='update'),
    path('delete/<int:pk>', views.delete_user, name='delete')
]