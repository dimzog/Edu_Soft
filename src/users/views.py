from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from courses.models import Statistics, StatisticsPerCategory


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login/')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    breadcrumbs = ['profile']

    def get(self, request, *args, **kwargs):
        user = request.user
        stats = Statistics.objects.filter(user=user)
        stats_cat = StatisticsPerCategory.objects.filter(user=user)

        context = {
            'stats': stats,
            'stats_cat': stats_cat
        }

        return render(request, self.template_name, context)



