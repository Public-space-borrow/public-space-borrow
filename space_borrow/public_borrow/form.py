from django import forms
class loginForm(forms.Form):
    username = forms.CharField(max_length=255, help_text="e.g., user@example.com", widget=forms.TextInput(attrs={"aria-describedby": "custom-description id_username_helptext"}))
    password = forms.CharField(widget=forms.PasswordInput())