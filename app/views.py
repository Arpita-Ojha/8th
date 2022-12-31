from django.shortcuts import render

# Create your views here.

def temp(request):

    dict={'a':500, 'b':2000, 'c':300}
    return render(request,'temp.html',context=dict)