from django.shortcuts import render

from qwitter_app.models import Profile


def dashboard(request):
    return render(request, 'base.html')


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user).select_related('user')
    template_path = 'qwitter_app/profile_list.html'
    context = {'profiles': profiles}
    return render(request, template_path, context)


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    template_path = 'qwitter_app/profile.html'
    context = {'profile': profile}
    return render(request, template_path, context)
