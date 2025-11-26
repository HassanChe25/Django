from django.db import models


class Prtoduct(models.Model):
    id = models.AutoField(primary_key=True)
    designation= models.CharField(max_length=100)
    
    def __str__(self):
        return self.designation
    
    


class Customer(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=100)
     loyaltyPoints=models.CharField(max_length=100)

     def __str__(self):
        return f"{self.name} ({self.loyaltyPoints})"

class Oreder(models.Model):
    id =models.AutoField(primary_key=True)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    prtoduct = models.ForeignKey(Prtoduct, on_delete=models.CASCADE, related_name='prtoduct')
    status = models.CharField(max_length=100)
    totalIHT  =models.CharField(max_length=100)
    totalITTC  =models.CharField(max_length=100)
    

    def __str__(self):
        return f"Order for {self.customer.name} ({self.customer.loyaltyPoints}) → {self.product.designation}"