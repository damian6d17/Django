from django.shortcuts import render
from dummy_images.models import DummyImage

def cos(request):
	return render(request, "cos.html", {'cos' : DummyImage.objects.all().order_by('?')[:1] })
# Create your views here.
