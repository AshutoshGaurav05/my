from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety, Store
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chai = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chai})

def chai_detail(requset, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(requset, 'chai/chai_detail.html', { 'chai':chai})

def chai_stores_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarityForm()
    return render(request, 'chai/chai_store.html',{'stores':stores, 'form':form})

