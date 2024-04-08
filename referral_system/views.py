from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def index(request):
    return HttpResponse("Welcome to Home Page!")


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(email=serializer.data['email'])
        token_obj, _ = Token.objects.get_or_create(user=user)
        print('Token', token_obj.key)
        return Response({'user_id': serializer.data['id'], 'token': token_obj.key, 'message': 'User registered successfully'},
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_referrals(request):
    user = request.user
    referrals = User.objects.filter(referral_code=user.referral_code).order_by('-timestamp')
    paginator = Paginator(referrals, 20)  # 20 users per page
    page_number = request.query_params.get('page')
    referrals_page = paginator.get_page(page_number)
    serializer = UserSerializer(referrals_page, many=True)
    return Response(serializer.data)


