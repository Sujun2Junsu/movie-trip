from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def login(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)

#         if not serializer.is_valid(raise_exception=True):
#             return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
#         # if serializer.validated_data['password'] == "none": # password required
#         #     return Response({'message': 'fail'}, status=status.HTTP_200_OK)

#         response = {
#             'success': True,
#             'token': serializer.data['token'] # 시리얼라이저에서 받은 토큰 전달
#         }
#         return Response(response, status=status.HTTP_200_OK)

