from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Student, LibraryHistory, FeesHistory


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model. Includes fields for user creation and role management.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Custom user creation logic.
        """
        user = User.objects.create_user(**validated_data)
        return user


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for Student model. Handles full CRUD operations.
    """
    class Meta:
        model = Student
        fields = '__all__'


class LibraryHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for LibraryHistory model. Validates borrowing and returning dates.
    """
    class Meta:
        model = LibraryHistory
        fields = '__all__'

    def validate(self, data):
        borrow_date = data.get('borrow_date')
        return_date = data.get('return_date')
        if return_date and return_date < borrow_date:
            raise ValidationError("Return date cannot be earlier than borrow date.")
        return data


class FeesHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for FeesHistory model.
    """
    class Meta:
        model = FeesHistory
        fields = '__all__'
