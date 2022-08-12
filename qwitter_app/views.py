from socket import timeout
from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from qwitter.settings import CACHE_TIMEOUT
from qwitter_app.models import Profile


# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def dashboard(request):
    return render(request, 'base.html')


def profile_list(request):
    if 'profiles' in cache:
        profiles = cache.get('profiles')
    else:
        profiles = Profile.objects.exclude(user=request.user).select_related('user')
        cache.set('profiles', profiles, timeout=CACHE_TIMEOUT)
    return render(request, 'qwitter_app/profile_list.html', {'profiles': profiles})


def profile(request, pk):
    if 'profile' in cache:
        profile = cache.get('profile')
    else:
        profile = get_object_or_404(Profile, id=pk)
        cache.set('profile', profile, timeout=CACHE_TIMEOUT)
    return render(request, 'qwitter_app/profile.html', {'profile': profile})
