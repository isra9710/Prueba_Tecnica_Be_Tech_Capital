from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from users.models import User
from django.db.models import Q
from Project.forms import RegisterForm
from django.urls import reverse
# Create your views here.
#Nos sirve para listar usuarios
class UserListView(ListView):
    template_name = 'users/index.html'
    queryset = User.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de usuarios'
        context['users'] = context['user_list']
        return context


#Filtro para la búsqueda por sexo o por nombre(la búsqueda usa un "like" de SQL)
class UserSearchListView(ListView):
    template_name = 'users/index.html'
    def get_queryset(self):
        filters = Q(sex__icontains=self.query()) | Q(first_name__icontains=self.query())
        return User.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')
    
#Actualizar datos de usuario
def update_user(request, pk):
    user = User.objects.get(id=pk)
    print(user)
    form = RegisterForm(instance=user)
    if request.method == "POST":
        print("Entra al POST")
        form = RegisterForm(request.POST ,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_crud:index')
    context = {'form':form}
    return render(request, 'users/edit.html', context)

#Eliminar usuario
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('users_crud:index')