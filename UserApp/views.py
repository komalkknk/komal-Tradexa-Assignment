from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import usermodelFrom,postform
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'UserApp/home.html')

def logout_view(request):
    return render(request,'UserApp/logout.html')

def signup_view(request):
    form=usermodelFrom()
    if request.method=='POST':
        form = usermodelFrom(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'UserApp/signup.html',{'form':form})

@login_required
def post_view(request):
    form = postform()
    if request.method == 'POST':
        form = postform(request.POST)
        form.save()
        return HttpResponseRedirect('/home')
    return render(request, 'UserApp/post.html', {'form': form})