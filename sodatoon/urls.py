from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sodatoon import views
from others import views as other_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'me', views.CurrentUserViewSet,basename='user')
router.register(r'artists', views.ArtistUserViewSet,basename='artists')
router.register(r'readers', views.ReaderUserViewSet,basename='readers')
router.register(r'users', views.UsersViewSet,basename='users')
router.register(r'story', other_views.StoryViewSet)
router.register(r'episode', other_views.EpisodeViewSet)
router.register(r'event', other_views.EventViewSet)
router.register(r'event-participants', other_views.EventParticipantsViewSet)
router.register(r'contest', other_views.ContestViewSet)
router.register(r'contest-participants', other_views.ContestParticipantsViewSet)
router.register(r'comments', other_views.CommentsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),

]
