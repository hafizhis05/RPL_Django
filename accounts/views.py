from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect ke halaman yang diminta atau ke halaman daftar mahasiswa
            next_page = request.POST.get('next') or request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('index')
        else:
            messages.error(request, 'Username atau password salah!')
    
    # Ambil parameter 'next' dari URL untuk ditampilkan di form
    next_page = request.GET.get('next', '')
    context = {'next': next_page}
    return render(request, 'accounts/login.html', context)

@login_required(login_url='/accounts/login/')
def logout_view(request):
    auth_logout(request)
    return redirect('login')
