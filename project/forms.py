from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={"type":"date", 'class':'form-control'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={"type":"date", 'class':'form-control'}))
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type":"date", 'class':'form-control'}))
    class Meta:
        model = Project
        fields = '__all__'