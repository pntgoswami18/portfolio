from django.db import models

# Blog model
# title
# publication date
# text blog post
# image
class Blog(models.Model):
    title = models.CharField(max_length=120)
    pub_date = models.DateField(auto_now_add=False)
    text_body = models.TextField()
    image = models.ImageField(upload_to='images/')