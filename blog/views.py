from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost, BlogComment, Category
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm, EditCommentForm
from taggit.models import Tag
from django.template.defaultfilters import slugify

###------------------- Redirect to previous page Mixin
class RedirectToProviousMixin:
    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']
###################################################################################################



#####------------------ Blog list view 
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog-grid.html'
    ordering = ['-date_posted']
    paginate_by = 9
#######################################################



#####-------------------- Blog Post Detail View
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost-details.html'


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogPostDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["BlogPosts"] =  BlogPost.objects.all().order_by('-date_posted')[:3]
        context["related_items"] = self.object.tags.similar_objects()[:5]
        #context['commot_tags'] = BlogPost.objects.tags.most_common()[:4]
        comments_connected = BlogComment.objects.filter(blogpost_connected=self.get_object()).order_by('-date_posted')
        context['comments'] = comments_connected
        if self.request.user.is_authenticated:
            context['form_comment'] = CommentForm(instance=self.request.user)

        return context
    
    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  blogpost_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
###################################################################################################


def tagged_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = BlogPost.tags.most_common()[:4]
    posts = BlogPost.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
        'common_tags':common_tags,
    }
    return render(request, 'tagged.html', context)


#######----------------- Category Detail View
##def CategoryDetailView(request, cats):
 #   category_posts = BlogPost.objects.filter(category=cats.replace('-', ' '))
  #  return render(request, 'category_detail.html',
   #               {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})
###################################################################################################

def CategoryDetailView(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    #common_tags = BlogPost.tags.most_common()[:4]
    posts = BlogPost.objects.filter(category=cat)
    context = {
        'cat':cat,
        'posts':posts,
        #'common_tags':common_tags,
    }
    return render(request, 'category_detail.html', context)



#########---------------- Delete Comment View    
class DeleteCommentView(RedirectToProviousMixin, DeleteView):
    model = BlogComment
    template_name = 'delete_comment.html'
###################################################################################################

   

#####-------------------- Update comment View
class UpdateCommentView(RedirectToProviousMixin, UpdateView):
    model = BlogComment
    template_name = 'update_comments.html'
    form_class = EditCommentForm
###################################################################################################

