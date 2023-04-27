from django.shortcuts import render

# Create your views here.
def builtin_filters(request):
    import datetime
    dt=datetime.datetime.now()

    d={'data':'pyTHon fUll stack dEVELOpment','dt':dt,'c':0}
    return render(request,'builtin_filters.html',d)