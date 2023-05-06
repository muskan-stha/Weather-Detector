from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.weatherapi.com/v1/current.json?key=e88c54a663074172849135235230605&q='+city+'').read()
        json_data=json.loads(source)
        data={
            'region':str(json_data['location']['region']),
            'temp':str(json_data['current']['temp_c'])+'k',
            'coordinate':str(json_data['location']['lat'])+''+str(json_data['location']['lon']),
            'pressure': str(json_data['current']['pressure_mb']),
            'humidity':(json_data['current']['humidity']), 
        }
    else:
        city=''
        data={}
    return render(request, 'index.html',{'city':city,'data':data})
