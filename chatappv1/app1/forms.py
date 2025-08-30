from django import forms
from .models import PDFDocument

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['pdf_file']

class QuestionForm(forms.Form):
    question = forms.CharField(max_length=255, label='Ask a Question')
