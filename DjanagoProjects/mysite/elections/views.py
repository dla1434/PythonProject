from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404

from .models import Candidate, Poll, Choice

import datetime

from django.db.models import Sum

# Version_0.1
# Create your views here.
# def index(request):
# 	candidates = Candidate.objects.all()
# 	str = ''
# 	for candidate in candidates:
# 		str += "<p>{} 기호 {}번( {} )<br>".format(candidate.name, 
# 			candidate.party_number, 
# 			candidate.area)
# 		str += candidate.introduction + "</p>"
# 	return HttpResponse(str)

# Version_0.2
# def index(request):
# 	candidates = Candidate.objects.all()
# 	return render(request, 'elections/index.html')

# Version_0.3
def index(request):
	print("index start")
	candidates = Candidate.objects.all()
	context = {'candidates': candidates}
	return render(request, 'elections/index.html', context)

# Version_0.1
# def candidates(request, name):
# 	try:
# 		candidate = Candidate.objects.get(name = name)
# 	except:
# 		return HttpResponseNotFound("없는 페이지 입니다.")
# 	return HttpResponse(candidate.name)

# Version_0.2
# def candidates(request, name):
# 	try:
# 		candidate = Candidate.objects.get(name = name)
# 	except:
# 		raise Http404
# 	return HttpResponse(candidate.name)

def candidates(request, name):
	candidate = get_object_or_404(Candidate, name = name)

	return HttpResponse(candidate.name)


# Version_0.1
# def areas(request, area):
	# return HttpResponse(area)

# Version_0.2
# def areas(request, area):
# 	candidates = Candidate.objects.filter(area = area)
# 	context = {
# 		'candidates': candidates,
# 		'area': area
# 	}
# 	return render(request, 'elections/area.html', context)

# Version_0.3
# def areas(request, area):
# 	today = datetime.datetime.now()
# 	poll = Poll.objects.get(area = area, start_date__lte=today, end_date__gte=today)
# 	candidates = Candidate.objects.filter(area = area)
# 	context = {
# 		'candidates': candidates,
# 		'area': area,
# 		'poll': poll
# 	}
	# return render(request, 'elections/area.html', context)

def areas(request, area):
	today = datetime.datetime.now()
	try:
		print("before poll {}", area)
		poll = Poll.objects.get(area = area, start_date__lte=today, end_date__gte=today)
		print("poll", poll)

		candidates = Candidate.objects.filter(area = area)
	except:
		print("---------------------except")
		poll = None
		candidates = None
	context = {
		'candidates': candidates,
		'area': area,
		'poll': poll
	}
	return render(request, 'elections/area.html', context)

# Version_0.1
# def polls(request, poll_id):
# 	poll = Poll.objects.get(pk = poll_id)
# 	selection = request.POST['choice']

# 	try:
# 		choice = Choice.objects.get(poll_id = poll_id, candidate_id = selection)
# 		choice.votes += 1
# 		choice.save()
# 	except:
# 		choice = Choice(poll_id = poll_id, candidate_id = selection, votes=1)
# 		choice.save()

# 	return HttpResponse("finish")

def polls(request, poll_id):
	poll = Poll.objects.get(pk = poll_id)
	selection = request.POST['choice']

	try:
		choice = Choice.objects.get(poll_id = poll_id, candidate_id = selection)
		choice.votes += 1
		choice.save()
	except:
		choice = Choice(poll_id = poll_id, candidate_id = selection, votes=1)
		choice.save()

	return HttpResponseRedirect("/areas/{}/results".format(poll.area))

def results(request, area):
	candidates = Candidate.objects.filter(area = area)
	polls = Poll.objects.filter(area = area)
	poll_results = []
	for poll in polls:
		result = {}
		result['start_date'] = poll.start_date
		result['end_date'] = poll.end_date

		# total_votest가 숫자가 아닌,  dictionary(=json) 형태로 넘겨준다.
		total_votes = Choice.objects.filter(poll_id=poll.id).aggregate(Sum('votes'))
		print("#############", total_votes)

		# 아래 처럼 aggreate된 dictionary에서  key값으로 가져와야 된다.
		result['total_votes'] = total_votes['votes__sum']
		rates = []
		for candidate in candidates:
			try:
				choice = Choice.objects.get(poll_id = poll.id,  candidate_id = candidate.id)
				rates.append( 
					round(choice.votes * 100/result['total_votes'] , 1))
			except:
				rates.append(0)
		result['rates'] = rates

		poll_results.append(result)
	context = {'candidates':candidates, 'area': area, 'poll_results': poll_results}
	return render(request, 'elections/result.html', context)

