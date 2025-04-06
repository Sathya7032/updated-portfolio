from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('contact/',contactHandler,name='contactHandler'),
    path('projects/',project, name='project'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_view,name="logout"),
    path('home/logout/', logout_user, name='logout_user'),
    path('blog/',blogs, name='blogs'), 
    path('post/<str:url>/', post_detail, name='post_detail'),
]
