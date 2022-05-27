from django.db import models


class Email(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254)
    message = models.TextField(null=False)
    dateSent = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sent_emails"

    # define string representation for this model class, will be used when display model class data in django admin web site.
    def __str__(self):
        return self.name
