from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.username} | at: {self.created_at}'