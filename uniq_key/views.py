from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Key
from .serializer import KeySerializer
from keys.settings import KEY_GENERATOR


@api_view(['GET', 'POST'])
def task_list(request):
    """
    Get a count keys, or create a new key.
    """

    if request.method == 'GET':
        return Response('There is also {} keys'.format(64**4-len(Key.objects.all())))

    elif request.method == 'POST':
        serializer = KeySerializer(data={'value':''.join(KEY_GENERATOR.__next__())})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def task_detail(request, value):
    """
    Get a key status, repaid key
    """

    if request.method == 'GET':
        status_text = {'I': 'This kei is in use', 'R': 'This key is repaid'}
        try:
            task = Key.objects.get(value=value)
            serializer = KeySerializer(task)
            return Response(status_text[serializer.data['status']])
        except Key.DoesNotExist:
            return Response('This key does not issued')

    elif request.method == 'PUT':
        try:
            task = Key.objects.get(value=value)
        except Key.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = KeySerializer(task, data={'value': value, 'status':'R'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
