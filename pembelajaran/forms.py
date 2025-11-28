from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    # Definisi Field User
    first_name = forms.CharField(
        label="Nama Depan", max_length=30, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Depan'})
    )
    last_name = forms.CharField(
        label="Nama Belakang", max_length=30, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Belakang'})
    )
    email = forms.EmailField(
        label="Email", required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contoh@email.com'})
    )
    username = forms.CharField(
        label="Username", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username unik (tanpa spasi)'})
    )

    # Definisi Password Manual (Jelas & Tegas)
    password = forms.CharField(
        label="Password", required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password minimal 8 karakter'}),
        min_length=8
    )
    confirm_password = forms.CharField(
        label="Konfirmasi Password", required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ulangi password'}),
        min_length=8
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    # Validasi Password Cocok/Enggak
    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get("password")
        pass2 = cleaned_data.get("confirm_password")

        if pass1 and pass2 and pass1 != pass2:
            self.add_error('confirm_password', "Password tidak cocok, coba cek lagi.")
        return cleaned_data