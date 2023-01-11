from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.contrib import messages
from.models import Profile

class LoginUserForm(AuthenticationForm): # İnhetritance Yöntemi ile AuthenticationForm dan bilgi alıyor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        

    def clean_username(self):
        username = self.cleaned_data.get("username")
      
        
        if username == "Gürkan":
            messages.success(self.request, "hoş geldin admin")
        return username

    def confirm_login_allowed(self, user):
        if user.username.startswith('s'):
            raise forms.ValidationError("bu kullanıcı adıyla login olamazsınız")


class NewUserForm(UserCreationForm):# İnhetritance Yöntemi ile UserCreationForm dan bilgi alıyor
    class Meta:
        model=User
        fields=("username","email","last_name",)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["password1"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["username"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget=widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["email"].required=True

    def clean_email(self):
        email=self.cleaned_data.get("email")     

        if User.objects.filter(email=email).exists():
            self.add_error("email","The e-mail you entered is in use")

        return email    


class UserForm(forms.ModelForm): 
    class Meta:
        model=User
        fields=("first_name","last_name","email")

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Adınız"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Soyadınız"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control","placeholder":"Mail Adresiniz"})
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=("avatar","location")

    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields["avatar"].widget = widgets.FileInput(attrs={"class":"form-control","placeholder":"Fotoğrafınız"})
            self.fields["location"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Lokasyonunuz"})
            
            