import re
from .models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.views import status


def validate_username(username):
    """
    Validate username
    """
    if re.search(r'([^a-zA-Z/.\d+])', username) is None:
        return username
    return False 

def validate_password(password):
    """
    Validate password
    """
    if re.search(r'(^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$_!%*?&]{8,}$)', password) is not None:
        return password
    return False

def check_if_exist(email, username):
    """
    Check if email and username exists
    """
    if User.objects.filter(email=email).exists()\
        or User.objects.filter(username=username).exists():
        return False

def validate_login_input(request, validated_data):
    """
    Validate login input fields
    """
    username = validated_data.get('username')
    password = validated_data.get('password')
    if username and password:
        return authenticate(request, username=username, password=password)
    return False
