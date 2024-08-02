from django.shortcuts import render,redirect
from .models import MovieReviewSystem
from .forms import MovieReviewSystemForm

# Create your views here.
def homeview(request):
    return render(request,"app1/home.html",{})

def addview(request):
    form =MovieReviewSystemForm()
    if request.method=="POST":
        form=MovieReviewSystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request, "app1/add.html", {"form":form})

def showview(request):
    obj=MovieReviewSystem.objects.all()
    print(obj)
    return render(request, "app1/show.html", {"obj":obj})

def deleteview(request,x):
    obj =MovieReviewSystem.objects.get(id=x)
    obj.delete()
    return redirect("/a1/sv/")
    return render(request, "app1/add.html", {"obj": obj})

def updateview(request,pk):
    obj = MovieReviewSystem.objects.get(id=pk)
    form = MovieReviewSystemForm(instance=obj)
    if request.method == "POST":
        form = MovieReviewSystemForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request, "app1/add.html", {"form": form})




