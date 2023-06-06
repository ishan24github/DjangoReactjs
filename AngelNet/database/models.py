from django.db import models
import array
import uuid

# Create your models here.

class startup(models.Model):
    startupID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100, unique=True)   # may be no limit length email
    company_website = models.URLField()
    company_Founders = models.CharField(max_length=100)    # Array field , multiple founders , in future
    linkedinURL = models.URLField()
    productDescription = models.CharField(max_length=300, blank=False)
    revenueDescription = models.CharField(max_length=300, blank=False)
    pitchUpload = models.FileField(upload_to='uploads/')     # learn this

    def __str__(self):
        return self.company_name


class investor(models.Model):
    investorID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    investor_name = models.CharField(max_length=100)
    investor_email = models.EmailField()
    # portfolio = array(startup,[])
    portfolio = []

    def __str__(self):
        return self.investor_name

    # investments size category
    # investment sectors


class auction(models.Model):
    auctionID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    startupID = models.ForeignKey('startup', on_delete=models.CASCADE)
    # investorID = models.ForeignKey('investor', on_delete=models.CASCADE)
    finalPercent = models.PositiveSmallIntegerField()
    finalPrice = models.PositiveIntegerField()
    investorNames = []            # append investor IDs after creating the auction object
    
    def __str__(self):
        return self.auctionID
    
    # final valuation
