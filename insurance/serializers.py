from rest_framework import serializers
from .models import Customer, Policy, PremiumPayment, Claim,Fundtranfer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'


class PremiumPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumPayment
        fields = '__all__'


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'

# class FundtranferSerializer(serializers.Serializer):
#     old_policy=serializers.PositiveIntegerField()
#     new_policy=serializers.postiveIntergerField()
#     customer_name=serializers.CharField(max_length=100)
#     tranfer_amount=serializers.DecimalField(max_digit=10)
#     transfer_reason=serializers.CharField()
#     status=serializers.CharField()
#     is_active=serializers.BooleanField()
    
    
class FundtransferSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Fundtranfer
        fields='__all__'