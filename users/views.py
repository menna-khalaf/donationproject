from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserProfileEditForm
from .models import User

# Registration
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_done')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.is_active = False  # For activation step

        # Auto-generate a unique username from email
        email = form.cleaned_data['email']
        base_username = email.split('@')[0]
        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        user.username = username

        user.save()
        # TODO: Send activation email in next step
        return super().form_valid(form)


# Profile Edit
class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileEditForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user
