from django.shortcuts import render,get_object_or_404
from .forms import PostForm
from activities.models import Notification
from django.http import Http404
from .models import Post
# Create your views here.


def comment_send(request):
	if not request.user.is_authenticated():
		raise Http404
	form = PostForm(request.POST or None)
	if form.is_valid():
		con = form.save(commit=False)
		con.user=request.user
		con.save()
		con.notify_commented(con)
	return render(request, 'comments.html',
                      {
                      	'form':form,
                      })


def check_notify(request,id=None):
	if not request.user.is_authenticated():
		raise Http404
	post1 = get_object_or_404(Post,id=id)
	user=request.user
	notification = Notification.objects.filter(to_user=user)
	return render(request,"user.html",{"notification":notification})

