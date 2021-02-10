from django.urls import path, include
from . import views

urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('login',views.loginUser, name='login'),
    path('logout',views.logout, name='logout'),
]
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
