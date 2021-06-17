from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Profile
from .forms import UserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

def register(request):
    form = UserForm()
    if (request.method == "POST"):
        user = UserForm(request.POST)
        if (user.is_valid()):
            user.save()
            messages.add_message(request, messages.SUCCESS, "thank you to be on our website")
            return redirect('/')
        else:
            form = user
            
    return render(request, 'register.html' ,{
        "form" : form
    })

@login_required
def profile(request, pk):
    profile_obj = Profile.objects.get(pk=pk)
    user_obj = User.objects.get(pk=pk)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('profile', pk=pk)
    else:
        p_data = {'native': profile_obj.native, 'goal': profile_obj.goal}
        u_data = {'first_name': user_obj.first_name, 'last_name': user_obj.last_name, 'email': user_obj.email}
        p_form = ProfileUpdateForm(initial=p_data)
        u_form = UserUpdateForm(initial=u_data)

    context={'p_form': p_form, 'u_form': u_form}
    return render(request, 'profile.html',context )

class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    def get_success_url(self):
        profile_id = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': profile_id})