from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("article:list")
    else:
        form = UserCreationForm()
    return render(request, 'file.html', {'form':form})

def logi(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # Login
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('article:list')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logo(request):
    if request.method == 'POST':
        logout(request)
        return redirect('article:list')
