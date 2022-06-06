from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from apps.accounts import endpoints_views as user_views
from apps.stories import endpoints_views as story_views
from apps.contests import endpoints_views as contest_views
from apps.events import endpoints_views as event_views
from apps.comments import endpoints_views as comment_views
from apps.episodes import endpoints_views as episodes_views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from apps.accounts.endpoints_views import MyTokenObtainPairView
class CustomizedAPIRootView(routers.APIRootView):
    """
    This is the api for sodatoon application!
    """
    pass


class DocumentedRouter(routers.DefaultRouter):
    APIRootView = CustomizedAPIRootView


router = DocumentedRouter()
admin_router = DocumentedRouter()
router.APIRootView.__name__ = 'Sodatoon API'
router.register(r'signUp', user_views.RegisterUserViewSet, basename='sign-up')
router.register(r'users', user_views.UsersViewSet, basename='users')
router.register(r'story', story_views.StoryViewSet)
router.register(r'episode',episodes_views.EpisodeViewSet )
router.register(r'event', event_views.EventViewSet)
router.register(r'eventParticipants', event_views.EventParticipantsViewSet)
router.register(r'contest', contest_views.ContestViewSet)
router.register(r'contestParticipants', contest_views.ContestParticipantsViewSet)
router.register(r'comments', comment_views.CommentsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls),name='base_routers'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', user_views.RegisterView.as_view(), name='auth_register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('logout/', user_views.LogoutView.as_view(), name='auth_logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
