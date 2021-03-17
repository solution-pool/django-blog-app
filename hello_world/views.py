from django.shortcuts import render

# Create your views here.
def hello_world(request):
	print(request.method)
	return render(request, 'hello_world.html', {})