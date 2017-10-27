from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'surveyForm/index.html')


def process(request):
	if request.session.get('count')== None:
		request.session['count'] = 0

	request.session['name']=request.POST['name']
	request.session['location']=request.POST['location']
	request.session['language']=request.POST['language']
	request.session['comment']=request.POST['comment']
	request.session['count'] += 1
	context = {
		'name': request.session['name'],
		'location': request.session['location'],
		'language': request.session['language'],
		'comment': request.session['comment']
	}
	return render(request, 'surveyForm/result.html', context)

def resut(request):
	return redirect('/')


def reset(request):
	del request.session['count']
	return redirect("/")

