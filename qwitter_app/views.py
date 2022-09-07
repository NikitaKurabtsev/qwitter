from django.shortcuts import render, get_object_or_404, redirect
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from qwitter.settings import CACHE_TIMEOUT
from qwitter_app.models import Profile, Qweet
from qwitter_app.forms import QweetForm


# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def dashboard(request):
    form = QweetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            qweet = form.save(commit=False)
            qweet.user = request.user
            qweet.save()
            return redirect('qwitter_app:dashboard')

    followed_qweets = Qweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by('-created_at')

    return render(
        request, 
        'qwitter_app/dashboard.html', 
        {'form': form, 'qweets': followed_qweets}
    )


# def profile_list(request):
#     if 'profiles' in cache:
#         profiles = cache.get('profiles')
#     else:
#         profiles = Profile.objects.exclude(user=request.user).select_related('user')
#         cache.set('profiles', profiles, timeout=CACHE_TIMEOUT)
#     return render(request, 'qwitter_app/profile_list.html', {'profiles': profiles})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user).select_related('user')  
    return render(request, 'qwitter_app/profile_list.html', {'profiles': profiles})


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        profile = Profile(user=request.user)
        profile.save()

    profile = get_object_or_404(Profile, id=pk)
    if request.method == 'POST':
        current_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_profile.follows.add(profile)
        elif action == 'unfollow':
            current_profile.follows.remove(profile)
        current_profile.save()
    return render(request, 'qwitter_app/profile.html', {'profile': profile})
