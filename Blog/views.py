from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView
from .forms import ContactRegistration,CommentsRegistration
from .models import Post,Comment,Contact,Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
def index(request):
    return render(request,"Blog/base.html")
"""def HomeView(ListView):
    model=Post
    template_name='home.html'
"""
def home(request,category=None):
    post=Post.published.all().order_by('-id')
    categories=Category.objects.all()
    #commentaire=post.comments.all()
    if category:
        category=get_object_or_404(Category,slug=category)
        post=post.filter(category=category).order_by('-id')
    paginator=Paginator(post,2)
    page=request.GET.get('page')
    try:
        post=paginator.page(page)
    except PageNotAnInteger:
        post=paginator.page(1)
    except EmptyPage:
        post=paginator.page(paginator.num_pages)
    context={
        'post':post,
        'page':page,
        'categories':categories,
        'category':category,
    }
    return render(request,"Blog/index.html",{'post':post,})

def search(request):
    query=request.GET.get('query')
    if not query:
        post=Post.objects.all()
    else:
        post=Post.objects.filter(titre__icontains=query)
        #if not post.exists():
            #post=Post.objects.filter(post__auteur__icontains=query)
        if not post.exists():
            message="Misére de misère, nous n'avons trouvé aucun résultat !!!"
        else:
            post=["<li>{}</li>".format(u.titre) for u in post]
            message="""Nous avons trouvé les publications correspondant à votre requête: Les voici:
                <ul>{}</ul>
            """.format("<li></li>".join(post))
        titre=""
        context={
            'post':post,
            'titre':titre,
            'msg':message,
        }
        return render(request,'Blog/search.html',context)
def searchbar(request):
    if request.method == 'GET':
        search=request.GET.get('query')
        post=Post.objects.filter(titre__icontains= search)
    return render(request,'Blog/search.html',{'post':post,})

def contact(request):
    if request.method=='POST':
        cm=ContactRegistration(request.POST)
        if cm.is_valid():
            nm=cm.cleaned_data['nom']
            eml=cm.cleaned_data['email']
            suj=cm.cleaned_data['sujet']
            msg=cm.cleaned_data['message']
            person=Contact(nom=nm,email=eml,sujet=suj,message=msg)
            person.save()
            person=ContactRegistration()
    else:
        cm=ContactRegistration()
    return render(request,"Blog/contact.html",{'contact':cm})
def about(request):
    return render(request,"Blog/a_propos.html")

def detail(request,slug:str):
    article=get_object_or_404(Post,slug=slug)
    commentaire=article.comments.all()
    if request.method=='POST':
        cmf=CommentsRegistration(request.POST)
        if cmf.is_valid():
            cmf.save(commit=False)
            cmf.instance.post=article
            cmf.save()
            return redirect('detail',slug=article.slug)
    else:
        cmf=CommentsRegistration()
    context={
        'post_id':article.id,
        'post_img':article.image.url,
        'post_author':article.auteur,
        'post_title':article.titre,
        'post_cnt':article.body,
        'post_date':article.date_publication,
        'comments':cmf,
        'cm_list':commentaire,
        'post_category':article.category, 
    }
    return render(request,"Blog/detail.html",context)