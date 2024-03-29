from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.TextField(max_length=10,db_column="user_id",null=True)
    first_name=models.TextField(max_length=20,db_column="fname")
    last_name=models.TextField(max_length=20,db_column="lname")
    subject=models.TextField(max_length=200,db_column="subject")
    message=models.TextField(max_length=500,db_column="message")
    email=models.TextField(max_length=20,db_column="email")
    phone=models.TextField(max_length=20,db_column="phone")
    
    class Meta:
        db_table="users"
        
        
        