from django.shortcuts import render,redirect

from .models import Comment
from .forms import CommentForm


#Create your views here.

def index(request):
	comments = Comment.objects.order_by('-date_added')

	context = {'comments': comments}
	return render(request, 'guestbook/index.html', context)

def sign(request):
	if request.method == 'POST':
		forms= CommentForm(request.POST)
		if forms.is_valid():
			new_comment=Comment(name=request.POST['name'], comment=request.POST['comment'])
			new_comment.save()
			return redirect('index')

	else:
		forms= CommentForm()


	



	context={'forms': forms}
	return render(request, 'guestbook/sign.html', context)

# def index(request):
#     context = locals()
#     template = 'index.html',
#     return render(request, template, context)

# def sign(request):
#     context = locals()
#     template = 'sign.html',
#     return render(request, template, context)

