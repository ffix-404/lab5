from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from django import forms

from django.urls import reverse

list_person=[]
class Add_person(forms.Form):#task=forms.CharField(label="new task")

    username=forms.CharField(label="username")

    password=forms.CharField(label="password",widget=forms.PasswordInput,min_length=6)

class Person:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def __str__(self):
        return(f"user name: ({self.username})___password:({"*"*int(len(self.password)-3)+self.password[-3:]})")




def home(request):


    return render(request,"index1.html",{"person":list_person})


def page1(request):#this is add method
    if request.method=="POST":
        form=Add_person(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            person=Person(username,password)
            list_person.append(person)
            return HttpResponseRedirect(reverse("myapp:index1"))
        else:
            return render(request,"index2_.html",{"form":form})    
    else:
        return render(request,"index2_.html",{"form":Add_person()})  

       
       


# Create your views here.


