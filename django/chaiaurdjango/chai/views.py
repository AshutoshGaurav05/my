from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety
# Create your views here.
def all_chai(request):
    chai = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chai})

def chai_detail(requset,chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(requset, 'chai/chai_detail.html', { 'chai':chai})