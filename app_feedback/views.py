from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

def gestionar_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Feedback registrado exitosamente!')
            return redirect('feedback')
    else:
        form = FeedbackForm()

    return render(request, 'app_feedback/formulario.html', {'form': form})