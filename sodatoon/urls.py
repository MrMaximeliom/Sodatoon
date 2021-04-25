"""sodatoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sodatoon import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'me', views.CurrentUserViewSet,basename='user')
router.register(r'story', views.StoryViewSet)
router.register(r'episode', views.EpisodeViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'event-participants', views.EventParticipantsViewSet)
router.register(r'contest', views.ContestViewSet)
router.register(r'contest-participants', views.ContestParticipantsViewSet)
router.register(r'comments', views.CommentsViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('points/', include('sodatoon.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),

]
