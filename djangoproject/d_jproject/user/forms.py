from django import forms

class Login(forms.Form): #inherit --> forms --> Form(class)
    email = forms.EmailField(label="Enter your Email")
    password = forms.CharField(widget=forms.PasswordInput,label="Enter your password")
option = [
    ("male","Male"),
    ("female","Female"),
    ("other","Other")
]
class Signup(forms.Form):
    email = forms.EmailField()
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pass = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=option)
    pic = forms.ImageField()
    #gender = forms.CharField(widget=forms.ChoiceField())
#<input type="email" name="email">
# acccept forms in 3 ways 
# form.as_table --> as table(accept) 
# form.as_p --> as paragraph
# form.as_ul --> list
class Email_Form(forms.Form):
    email = forms.EmailField()

class Otp(forms.Form):
    otp = forms.CharField(max_length=5)

class changepassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pass = forms.CharField(widget=forms.PasswordInput)
