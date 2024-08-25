from django.shortcuts import render
import urllib.parse
import requests
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def check(request):
    if request.method == 'POST':
        encoded_urls = request.POST.get('link')
        url = urllib.parse.unquote(encoded_urls)
        response = requests.get(url, timeout=10)

        content = {
            'response': response,
            'text': response.text, 
            'url': url
        }
        return render(request, 'main/results.html', content)
