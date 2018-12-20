from django.shortcuts import render,get_list_or_404
from .models import Applicant
from .forms import PostForm
from django.http import HttpResponse

# Create your views here.

def Applicant_list(request):
    posts = Applicant.objects.all()
    return render(request, 'basicform/Applicant_list.html', {'posts': posts})

def Applicant_detail(request, pk):
    post = Applicant.objects.get(pk=pk)
    return render(request, 'basicform/Applicant_detail.html', {'post': post})

def Applicant_new(request):
    #form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return Applicant_detail(None,pk=post.pk)

            #return HttpResponse("Your application has been received! Go back to the home page.")
    else:
        form = PostForm()
    return render(request, 'basicform/Application_edit.html', {'form': form})

