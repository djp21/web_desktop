from django.shortcuts import render
from django.http import HttpResponse
def homepageview(request):
	red = '<h2 style="color:red">Namaste Nitesh main aap se pyaar nahi karti hun</h2>'
	black ='<h2 style="color:black">Namaste Nitesh main aap se pyaar karti hun</h2>'
	final = ''
	for i in range(100):
		if(i%2==0):
			
			final = final + red
		else:
			final = final + black
	return HttpResponse(final)
# Create your views here.
