from django.db import models

# Create your models here.
class usermodel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    username  = models.EmailField(max_length=100)
    #
    class Meta:
        app_label = 'user_data'

    # def __str__(self):
    #     return self.name

class postmodel(models.Model):
    user = models.ForeignKey(usermodel,on_delete = models.CASCADE,related_name='user')
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    #
    class Meta:
        app_label = 'post_data'

    # def __str__(self):
    #     return self.name
