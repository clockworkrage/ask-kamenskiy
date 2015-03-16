from django.shortcuts import render

from django.http import HttpResponse

def index(request):

	response = HttpResponse()
	if request.method == 'GET':
		response.write('GET: ')
		for outpar in request.GET:
			response.write(request.REQUEST[outpar])
			response.write(' ')
	elif request.method == 'POST':
		response.write('POST: ')
		for outpar in request.POST:
			response.write(request.REQUEST[outpar])
			response.write(' ')
	return response