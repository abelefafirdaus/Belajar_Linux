from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

# --- AUTH VIEWS ---

def register_view(request):
    if request.user.is_authenticated:
        return redirect('pembelajaran:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 1. Simpan user tapi jangan commit ke DB dulu (karena password blm di-hash)
            user = form.save(commit=False)
            
            # 2. Set password (enkripsi)
            user.set_password(form.cleaned_data['password'])
            
            # 3. Simpan beneran
            user.save()
            
            # 4. Langsung login
            login(request, user)
            messages.success(request, f"Selamat datang, {user.first_name}!")
            return redirect('pembelajaran:index')
        else:
            messages.error(request, "Registrasi gagal. Cek error di form.")
    else:
        form = RegisterForm()
    
    return render(request, 'pembelajaran/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('pembelajaran:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Halo, {user.first_name}!")
                # Redirect ke halaman yang diminta sebelumnya atau ke index
                next_url = request.GET.get('next', 'pembelajaran:index')
                return redirect(next_url)
            else:
                messages.error(request, "Username atau password salah.")
        else:
            messages.error(request, "Username atau password salah.")
    else:
        form = AuthenticationForm()
        # Styling form login bawaan
        form.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        form.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

    return render(request, 'pembelajaran/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Anda berhasil logout.")
    return redirect('pembelajaran:login')

# --- PUBLIC VIEW (Hanya Beranda) ---

def index(request):
    return render(request, 'pembelajaran/index.html')

# --- PROTECTED VIEWS (Harus Login) ---
# Semua view di bawah ini akan melempar user ke halaman login jika belum login

@login_required
def aboutus(request):
    return render(request, 'pembelajaran/aboutus.html')

@login_required
def linux_dasar(request):
    return render(request, 'pembelajaran/belajar_cli.html')

@login_required
def belajar_linux(request):
    return render(request, 'pembelajaran/kamus_cli.html')

@login_required
def install_linux(request):
    return render(request, 'pembelajaran/install_linux.html')

@login_required
def linux_chapter1(request):
    return render(request, 'pembelajaran/linux_chapter1.html')

@login_required
def linux_chapter2(request):
    return render(request, 'pembelajaran/linux_chapter2.html')

@login_required
def linux_chapter3(request):
    return render(request, 'pembelajaran/linux_chapter3.html')