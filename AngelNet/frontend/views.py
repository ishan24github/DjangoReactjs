from django.shortcuts import render
# Create your views here.

# only working in forntend/ not pages/

def index(request):
    return render(request, 'frontend/index.html')


# def register(request):
#     return render(request, 'frontend/register.html')


# def startupForm(request):
#     return render(request, 'frontend/startupForm.html')

# def portfolio(request):
#     return render(request, 'frontend/portfolio.jsx')