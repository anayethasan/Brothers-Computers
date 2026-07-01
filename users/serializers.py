from rest_framework import serializers
from users.models import User
 
 
class UserSerializer(serializers.ModelSerializer):
    initial = serializers.SerializerMethodField()
 
    class Meta:
        model = User
        fields = ["id", "email", "name", "image", "initial", "is_active", "is_staff", "date_joined"]
        read_only_fields = ["id", "date_joined"]
        ref_name = "CustomUser"
 
    def get_initial(self, obj):
        """
        Returns the first character of the name, uppercased.
        Frontend uses this as a fallback avatar when no image is uploaded.
        """
        return obj.name[0].upper() if obj.name else "?"
 
 
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
 
    class Meta:
        model = User
        fields = ["id", "email", "name", "image", "password", "is_active", "is_staff"]
 
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user
 
 
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=8)
 
    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value
    
class EmptySerializer(serializers.Serializer):
    pass