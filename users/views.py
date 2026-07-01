from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from users import serializers as sz
from users.models import User

class AdminLoginView(TokenObtainPairView):
    pass

class AdminLogoutView(generics.GenericAPIView):
    
    serializer_class = sz.EmptySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class AdminProfileView(generics.RetrieveUpdateAPIView):
    
    serializer_class = sz.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
class AdminCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = sz.UserCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    

class ChangePasswordView(generics.GenericAPIView):
    serializer_class = sz.ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        user.set_password(serializer.validated_data["new_password"])
        user.save()
        return Response({"detail": "Password updated successfully done!"})
    
