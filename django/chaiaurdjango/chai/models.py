from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
  price = models.DecimalField(default=0,max_digits=5, decimal_places=2)
  description = models.TextField(default='')

  def __str__(self):
    return self.name
  
# one to many relationship
class ChaiReview(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
  reting = models.IntegerField()
  comment = models.TextField(default='')
  date_added = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{self.user.username} reviewed {self.chai.name}'


# Many to Many relationship
class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')
  
  def __str__(self):
    return self.name

# One to One relationship
class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default=timezone.now)
  valid_until = models.DateTimeField()
  
  def __str__(self):
    return f'{self.chai.name} certificate'
