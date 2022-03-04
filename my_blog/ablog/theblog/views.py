from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse
from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, CommentForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import Http404
from django.views.generic.edit import FormMixin

# Create your views here.





class HomeView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'home.html'
    ordering = ['-created_at']

    
    def get_context_data(self, *args,**kwargs):
        self.paginate_by = self.request.GET.get("limit",self.paginate_by)
        
        context = super().get_context_data(*args,**kwargs)

        # Preparing query
        context['query'] = self.request.GET.get("q")
        context['limit_option_list'] = [5,10,15]

        # Random posts
        main_list = Post.objects.order_by('?')[:1]
        secondary_list = Post.objects.order_by('?')[:2]
        
    
        # Most popular articles
        most_popular = Post.objects.filter(views__gt=0).order_by('-views')[:3]
        context['most_popular'] = most_popular

        # Category menu
        cat_menu = Category.objects.all()

        context.update({"main_list":main_list, "secondary_list":secondary_list, "cat_menu":cat_menu, "paginate_by":self.paginate_by})


        return context

    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            return super().get_queryset()

        return Post.objects.filter(title__icontains=query)



def contactView(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            f"From {message_name}",
            message, 
            message_email, # from email
            ['djangomyblog@gmail.com'], # to email
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_name':message_name,
        })
    else:
        return render(request, 'contact.html', {})



def categoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',
     {"cat_menu_list":cat_menu_list})

def categoryView(request, cats):
    category_articles = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html',
     {'cats': cats.replace('-', ' ').title(),
      'category_articles':category_articles})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        # Getting specific element and adding views

        article_object = super().get_object()
        article_object.views += 1
        article_object.save ()
        context['post'] = article_object

        # Getting all comments by specific article
        comments = article_object.comment_set.all().order_by('id')
        context['comments'] = comments

        context['form'] = CommentForm()
        
        # Most popular posts
        most_popular = Post.objects.filter(views__gt=1).order_by('-views')[:3]
        context['most_popular'] = most_popular

        #Category menu
        cat_menu = Category.objects.all() 
        context.update({"cat_menu":cat_menu})

        return context
    
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-timestamp')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'article_detail.html', context)

    

    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_article.html'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdateView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')


