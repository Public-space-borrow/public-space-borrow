from django import forms
class StudentID(forms.Form):
    stu_ids = forms.CharField(label="學生學號", widget=forms.Textarea)