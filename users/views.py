from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qwitter_app:dashboard')

    return render(request, 'register.html', {'form': form})
