from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Claim,PremiumPayment,Customer,Policy,Fundtranfer
from .serializers import ClaimSerializer,PolicySerializer,CustomerSerializer,PremiumPaymentSerializer,FundtransferSerializer


class ClaimViewSet(ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class PremiumPaymentListAPIView(ListCreateAPIView):
    queryset = PremiumPayment.objects.all()
    serializer_class = PremiumPaymentSerializer


class PremiumPaymentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PremiumPayment.objects.all()
    serializer_class = PremiumPaymentSerializer


class PolicyListAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PolicyDetailAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class FundTransferListApiView(APIView):
    
    def get(self,request):
        fundtransfer=Fundtranfer.objects.all()
        serializer=FundtransferSerializer(fundtransfer,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=FundtransferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,Status=400)

class CustomerListAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class FundTransferDetailAPIView(APIView):
    def get(self,request,pk):
        fundtranfer=Fundtranfer.objects.get(pk=pk)
        serializer=FundtransferSerializer(fundtranfer)
        return Response(serializer.data)
    
    def put(self,request,pk):
        fundtransfer=Fundtranfer.objects.get(pk=pk)
        serializer=FundtransferSerializer(fundtransfer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors,status=400)
    
    def put(self,request,pk):
        fundtranfer=Fundtranfer.objects.get(pk=pk)
        fundtranfer.delete()
        return Response(status=204)



class CustomerDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response(status=204)
    
    
