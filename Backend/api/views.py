from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import users
from .serializers import UserSerializer



@api_view(['GET'])
def getData(request):
    user = users.objects.values(
        "username", "email", "first_name", "last_name", "staff_status"
    )
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
       
    return Response(serializer.data)
    