from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse
from django.utils import datetime_safe
from django.core.paginator import Paginator
from .models import Post , Contact
from .forms import ContactForm

 
# common views data
common_current_date = datetime_safe.datetime.now()


# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by('-published_date')

    paginator = Paginator(latest_posts, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    page_conf = {
        'title_tag' : "BlogApp - Home",
        'title_page' : "Blog App",
        'page_explain' : "Hello and welcome to this blog",
        'current_date' : common_current_date,
        'data' : page ,
        
    }

    return render(request, 'blogApp/index.html',context=page_conf)




def datail(request , post_id):
    post = get_object_or_404(Post,pk=post_id)
    #post = {'post' : post}


    page_conf = {
        'title_tag' : post.title,
        'title_page' : post.title,
        'current_date' : post.published_date,
        'post' : post ,
        'page_head_image' : post.image
    }

    return render(request, 'blogApp/detail.html',context=page_conf)




def contact(request):

    if request.method == 'GET':
        form = ContactForm()
        form ={'form':form}
        return render(request, 'blogApp/contact.html',context=form)
    else:
        # Get form data
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.data['name']
            email = form.data['email']
            message = form.data['message']

            new_msg = Contact()
            new_msg.name = name
            new_msg.email = email
            new_msg.message = message

        
            new_msg.save()


            return redirect('blogApp:index')

            

        return render(request, 'blogApp/contact.html')        




