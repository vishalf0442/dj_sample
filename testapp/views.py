from django.shortcuts import render
from testapp.models import Student

# Create your views here.

def calc_percent(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        maths = int(data['maths'])
        science = int(data['science'])
        history = int(data['history'])
        avg = (maths+science+history) / 3
        return render(request, "testapp/index.html", context={"name":name, "avg":avg})
    return render(request, "testapp/index.html")




