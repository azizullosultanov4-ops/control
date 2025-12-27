from django.shortcuts import render
from apps.core.models import Control
# Create your views here.
def index(request):
    control = Control.objects.latest("id",)
    return render(request, "index.html", locals())
