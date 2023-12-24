from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def create_user(request):
    try:
        print("Creating an user")
        username = 'dummy'
        email = 'dummy@gmail.com'
        password = 'dummy54321'
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        user.save()
        print(f"Created an user: {user}")
        return Response({
            "message": "User Created!"
        }, status=201)
    except Exception as err:
        print(err)
        return Response({
            "message": err
        }, status=500)
