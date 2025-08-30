from django.shortcuts import render, redirect
from .forms import PDFUploadForm, QuestionForm
from .utils import get_pdf_text, get_text_chunks, get_vector_store, user_input

def home(request):
    """Render the main frontend page."""
    return render(request, 'frontend.html')

def process_pdfs(request):
    """Handle PDF uploads and process text."""
    if request.method == "POST":
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.save()  
            raw_text = get_pdf_text([pdf_file.pdf_file.path]) 
            text_chunks = get_text_chunks(raw_text)  
            get_vector_store(text_chunks)  
            return redirect('home') 
    return render(request, 'frontend.html', {'error': 'Failed to process PDF'})

def ask_question(request):
    """Handle user questions and return responses."""
    response = None
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            try:
                response = user_input(question)  
            except Exception as e:
                response = f"An error occurred: {e}" 
    return render(request, 'frontend.html', {'response': response})
