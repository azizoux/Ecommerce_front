from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from .models import Mug, Cart
from .serializers import MugSerializer, CartSerializer
from django.views.decorators.csrf import csrf_exempt


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().filter(payed=False)
    serializer_class = CartSerializer



class MugViewSet(viewsets.ModelViewSet):
    queryset = Mug.objects.all()
    serializer_class = MugSerializer

    @action(detail=True, methods=['POST'])
    def save_file(self, request, pk=None):
        if 'file' in request.data:
            file = request.FILES['file']
            file_name = default_storage.save(file.name, file)
            return JsonResponse(file_name, safe=False)
        else:
            response = {'message': 'You need to provide file'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def getCartByMugId(self, request, pk=None):
        cart = Cart.objects.get(mug=pk)
        cart_serializer = CartSerializer(cart, many=False)
        return JsonResponse(cart_serializer.data, safe=False)
