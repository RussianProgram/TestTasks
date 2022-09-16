from django.shortcuts import redirect, render

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.generic import ListView
from django.views.generic.edit import UpdateView,CreateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionDenied

from .models import Host


"""
View для регистрации пользователя
"""
def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/accounts/login')

    return render(request,
                  'registration/register.html',
                  {'form':form})

"""
View для логирования пользователя
"""
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home')
    else:
        form = AuthenticationForm(request)

    return render(request,
                  "registration/login.html",
                  {"form": form})

"""
View для выхода из аккаунта 
"""
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts/login')

    return render(request, "registration/logout.html")


"""
Class-based View для отображения списка хостов 
(Отдельный вид для админа и юзера)
"""
class HostListView(LoginRequiredMixin, ListView):
    context_object_name = 'hosts'
    template_name = 'home.html'

    def get_queryset(self):
        User = self.request.user
        if str(User.groups.last()) == 'Admin':
            return Host.objects.all()

        return User.hosts.all()




"""
Базовый Миксин для CRUD
"""
class HostBaseMixin(LoginRequiredMixin):
    model = Host
    success_url = '/home'


class HostDeleteUpdateMixin(HostBaseMixin):
    def get(self, request, *args, **kwargs):
        User = request.user
        host_id = kwargs.get('pk', None)
        current_host = Host.objects.get(pk=host_id)

        if str(User.groups.last()) == 'Admin' or current_host in User.hosts.all():
            return super().get(request, *args, **kwargs)

        raise PermissionDenied


class HostCreateUpdateMixin(HostBaseMixin):
    fields = ['ip',
              'port',
              'resource']

    def get_form(self, form_class=None):
        User = self.request.user
        if str(User.groups.last()) == 'Admin':
            self.fields = ['ip','port','owners','resource']

        return super().get_form()


class CreateHostView(HostCreateUpdateMixin, CreateView):
    template_name = 'host_forms/host_creation_form.html'

class UserUpdateHostView(HostCreateUpdateMixin,
                         HostDeleteUpdateMixin,
                         UpdateView):
    template_name = 'host_forms/host_update_form.html'

class UserDeleteHostView(HostDeleteUpdateMixin, DeleteView):
    template_name = 'host_forms/host_confirm_delete.html'







