from django.shortcuts import render
from .models import Types
from .serializer import TypesSerializer
from rest_framework.views import APIView, Request, Response, status
# Create your views here.


class TypesView(APIView):
    def get(self, request: Request) -> Response:
        types = Types.objects.all()

        serializer = TypesSerializer(types)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = TypesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)