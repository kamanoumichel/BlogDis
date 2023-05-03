from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager,self).get_queryset().filter(status='published')
class Category(models.Model):
    nom = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('home')
    
class Post(models.Model):
    STATUS_ChOICES=(
        ('draft','Draft'),
        ('published','Published'),
                    )
    titre=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    body=models.TextField()
    date_creation=models.DateField(auto_now_add=True)
    mis_a_jour=models.DateField(auto_now=True)
    status=models.CharField(choices=STATUS_ChOICES,default='draft',max_length=200)
    date_publication=models.DateField(default=timezone.now())
    auteur=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_posts')
    image=models.ImageField(upload_to='media',default='logo.png')
    objects=models.Manager()
    published=PublishManager()
    
    def __str__(self):
        return self.titre +' '+ str(self.auteur)
    #On rajoute une classe meta por préciser qu'on classe les articles par ordre d'ajout
    class Meta:
        ordering=['-date_creation']

    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    nom=models.CharField(max_length=200,default="inconnu")
    email=models.EmailField(max_length=150)
    commentaire=models.TextField()
    date_creation=models.DateField(auto_now_add=True)
    date_modify=models.DateField(auto_now=True)

    def __str__(self):
        return self.post.titre
    class Meta:
        ordering=['-date_creation']
        
class Contact(models.Model):
    nom=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    sujet=models.CharField(max_length=200)
    message=models.TextField()
