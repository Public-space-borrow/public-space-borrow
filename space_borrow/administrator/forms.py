from django import forms
class StudentID(forms.Form):
    ids = forms.CharField(label="學生學號", widget=forms.Textarea)
    
class reservation(forms.Form):
    space = forms.IntegerField(required=True)
    date = forms.DateField(required=True)
    startTime = forms.IntegerField(required=True)
    endTime = forms.IntegerField(required=True)
    reason = forms.CharField(required=True)
    