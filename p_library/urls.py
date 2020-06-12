from django.urls import path
from .views import FriendList, FriendFormEdit
 
app_name = 'p_library'
 
urlpatterns = [
    path('friend/create', FriendFormEdit.as_view(), name='friend_create'),
    path('friends', FriendList.as_view(), name='friend_form'),
]