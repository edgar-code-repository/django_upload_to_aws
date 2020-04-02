from django.db import models

class ClientsFile(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name
