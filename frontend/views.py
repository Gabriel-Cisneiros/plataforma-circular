from django.shortcuts import render

# Create your views here.

def base(request):
  return render(request, "base.html")

def home(request):
  return render(request, "home.html")

def aboutCottonMove(request):
  return render(request, "about.html")

def aboutPlatform(request):
  return render(request, "aboutPlatform.html")

def news(request):
  return render(request, "news.html")

def disposeHere(request):
  return render(request, "disposeHere.html")

def circularEconomy(request):
  return render(request, "circularEconomy.html")

def traceability(request):
  return render(request, "traceability.html")

def contact(request):
  return render(request, "contact.html")

def faq(request):
  return render(request, "faq.html")
