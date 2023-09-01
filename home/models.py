from django.db import models

class Contact(models.Model):
    # Fields of the Contact model (email, name, address, phone)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.CharField(max_length=12)


    def __str__(self):
        return self.name +" "+self.email

    # class Meta:
    #     app_label = 'home'  # Replace 'home' with the correct app name if needed
