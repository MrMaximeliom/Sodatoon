from apps.accounts.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from apps.accounts.serializers import UserSerializer, GroupSerializer
from apps.accounts.models import User
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated,AllowAny
from apps.accounts.serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from sodatoon.permissions import IsAnonymousUser
from rest_framework import mixins
from django.utils.translation import gettext_lazy as _


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterSerializer



class CurrentUserViewSet(viewsets.ModelViewSet):
    """
      API endpoint that allows to view current user data
      """
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)



class ArtistUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        return User.objects.filter(is_artist=True)

class ReaderUserViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows users to be viewed or edited.
        """
        queryset = User.objects.all().order_by('-date_joined')
        serializer_class = UserSerializer
        permission_classes = [AllowAny]
        def get_queryset(self):
            return User.objects.filter(is_artist=False)


class UsersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                            mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_artist']

    # def get_queryset(self):
    #     return User.objects.filter(is_artist=False)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class MyTokenObtainPairView(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = MyTokenObtainPairSerializer

class RegisterUserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
        API endpoint that allows to register new users
        this endpoint allows only POST function
        permissions to this view is restricted as the following:
        - anonymous users and system backend users (Admin and Staff )
         only can access this api to create an account
         Data will be submitted in the following format using POST function:
       {
        "id": 2,
        "full_name": "ali hassan hamid",
        "phone_number": "0922367654",
        "image": "image_path",
        "gender": "male",
        "email": "ali@gmail.com",
        "birth_date": "25-2-2020",
        "user_type":""driver"
         }
      """
    from apps.accounts.serializers import RegisterSerializer

    def get_view_name(self):
        return _("Register New User")

    from .models import User
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAnonymousUser]