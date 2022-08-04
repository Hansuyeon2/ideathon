from django.db import models



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,null=True)
    writer = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200,null=True)
    intention = models.CharField(max_length=200,null=True)
    genre = models.CharField(max_length=200,null=True)
    summary = models.CharField(max_length=200,null=True)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "post/", blank=True, null=True)
    



class Comment(models.Model):
   content = models.TextField(null=True)
   post = models.ForeignKey( Post ,on_delete=models.CASCADE, related_name ='comments',null=True)
   created_at = models.DateTimeField(auto_now_add=True,null=True)
   update_at = models.DateTimeField(auto_now=True,null=True)




        