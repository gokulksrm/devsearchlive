from django.db import models
import uuid


# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    featured_image= models.ImageField(null=True,blank=True,default="default.jpg")
    demo_link=models.CharField(max_length=1000,blank=True, null=True)
    source_link=models.CharField(max_length=1000,blank=True, null=True)
    tags=models.ManyToManyField(Tag,blank=True)
    vote_total=models.IntegerField(default=0)
    vote_ratio=models.IntegerField(default=0)
    created= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            img= self.featured_image.url
        except:
            img=''
        return img

class Review(models.Model):
    VOTE_TYPE=(
        ('up','up'),
        ('down','down'),
    )
    project = models.ForeignKey(Project,on_delete=models.CASCADE, null=True,blank=True)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=50,choices=VOTE_TYPE)
    updated=models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.value





