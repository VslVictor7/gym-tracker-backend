from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .serializers import UserSerializer, MyTokenObtainPairSerializer, CookieTokenRefreshSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 14
            response.set_cookie(
                'refresh_token',
                response.data['refresh'],
                max_age=cookie_max_age,
                httponly=True,
                secure=True,
                samesite='Lax'
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)

class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 14
            response.set_cookie(
                'refresh_token',
                response.data['refresh'],
                max_age=cookie_max_age,
                httponly=True,
                #secure=True,
                samesite='Lax'
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)

@api_view(['POST'])	
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_user(request):
    refresh_token = request.COOKIES.get('refresh_token')

    if not refresh_token:
        return JsonResponse({"detail": "Token inválido ou não encontrado."}, status=400)

    try:
        token = RefreshToken(refresh_token)
        
        token.blacklist()

        response = JsonResponse({"message": "Logout realizado com sucesso"})
        response.delete_cookie('refresh_token')
        return response
    except InvalidToken:
        return JsonResponse({"detail": "Token inválido."}, status=400)
    except TokenError:
        return JsonResponse({"detail": "Erro ao processar o token."}, status=400)
