from django.db import models


# Create your models here.

class Property(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    street_address = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, default='')
    postcode = models.CharField(max_length=10 )
    city = models.CharField(max_length=20)
    agent = models.ForeignKey('auth.user', null=True, related_name='properties', on_delete=models.SET_NULL)
    address_text = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        concatenates address fields into address text and saves to 
        ' address_text' field
        """
        address_text = self.street_address + ', '
        if not self.address_line_2 == '':
            address_text = address_text + self.address_line_2 + ', '
        address_text = address_text + self.city + ', '
        address_text = address_text + self.postcode 

        self.address_text = address_text
        super(Property, self).save(*args, **kwargs)
