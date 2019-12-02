
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register/', views.signup, name='signup'),
    url(r'^home/$',views.home,name='home'),
    url(r'^new-hood/',views.create_hood,name='new-hood'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^profile/(?P<username>\w+)/edit', views.edit_profile, name='edit-profile'),
    url(r'^single-hood/(?P<id>\d+)',views.one_hood,name='single-hood'),
    # url(r'^(?P<hood_id>)/member',views.hood_members,name='member'),
    url(r'^members/(?P<hood_id>\d+)',views.hood_members,name='members'),
    url(r'^new_post/(?P<hood_id>\d+)',views.create_posts,name='post'),
    # url(r'^(P?<hood_id>\d+)/new-post',views.create_posts,name='post'),
    url(r'^join-hood/(?P<id>\d+)',views.join_hood,name='join-hood'),
    url(r'^leave-hood/(?P<id>\d+)',views.leave_hood,name='leave-hood'),
    url(r'^search/$',views.search_business,name='search'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

