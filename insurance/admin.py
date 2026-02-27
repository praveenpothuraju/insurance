from django.contrib import admin
from .models import Customer,Policy,PremiumPayment,Claim,Fundtranfer

# Register your models here.
admin.site.register(Customer)
admin.site.register(Policy)
admin.site.register(PremiumPayment)
admin.site.register(Claim)
admin.site.register(Fundtranfer)
