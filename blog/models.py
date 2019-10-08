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

    def get_summary(self):
        return self.text_body[:40] + (self.text_body[40:] and '..')

    # used for reference on admin dashbaord
    def __str__(self):
        return self.title
