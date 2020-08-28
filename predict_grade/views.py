from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from predict_grade.models import Inventory, Students, StudentCreateForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

def goods_in_stock(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        price = request.POST['price']
        _id = Inventory.objects.create(code = code, name = name, price = price)        
        print("_id:", _id)

    inventory_list = Inventory.objects.all()
    return render(request, 'goods_in_stock.html',{
        'inventory_list': inventory_list
    })

class StudentCreate(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {'form': StudentCreateForm(),
                   'student_list': Students.objects.all()}
        return render(request, 'students.html', context)

    def post(self, request, *args, **kwargs):
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            student = form.save()
            # student.save()
            print(student)
            return self.get(request, *args, **kwargs)

        context = {'form': form,
                   'student_list': Students.objects.all()}
        return render(request, 'students.html', context)