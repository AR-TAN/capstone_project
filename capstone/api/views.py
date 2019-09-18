from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from adopt.models import Adopt

from .serializers import AdoptSerializer, UserSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_adopt(request, pk):
    try:
        adopt = Adopt.objects.get(pk=pk)
    except Adopt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdoptSerializer(adopt)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        adopt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = AdoptSerializer(adopt, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_adopt(request):
    # get all adopt
    if request.method == 'GET':
        adopt = Adopt.objects.all()
        serializer = AdoptSerializer(adopt, many=True)
        return Response(serializer.data)
    # insert a new record for a adopt
    elif request.method == 'POST':

        data = {
            'name': request.data.get('name'),
            'breed': request.data.get('breed'),
            'description': request.data.get('description'),
            'image': request.data.get('image'),
            'years_old': request.data.get('years_old'),
            'location': request.data.get('location'),
            'posted_by': request.data.get('posted_by')
        }

        user = User.objects.get(username='angelica')
        if not request.user.is_anonymous:
            user = request.user
        data['posted_by'] = user.id
        serializer = AdoptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_users_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
