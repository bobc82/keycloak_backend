from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from api.authentication import HasRolePermission
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response(request.user.user_info)

@api_view(['GET'])
@permission_classes([IsAuthenticated, HasRolePermission])
def role_view(request):
    return Response(request.user.user_info)

