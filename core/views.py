from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Conócenos</a></li>
    <li><a href="/career">Carreras</a></li>    
    <li><a href="/portfolio">Noticias</a></li>    
    <li><a href="/contact">Contacto</a></li>
    <li><a href="/contact">Intranet</a></li>    
</ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def career(request):
    return render(request, "core/career.html")

def contact(request):
    return render(request, "core/contact.html")

def intranet(request):
    return render(request, "core/intranet.html")