from django.http import HttpResponse
from app.models import State

def index(request):

    return HttpResponse(State.objects.first().state)


def post(request):
	state = State.objects.first();
	if state.state == 0:
		state.state = 1
		state.save()
	else:
		state.state = 0
		state.save()


	# state = State.objects.first()
	# state.state = newState
	# state.save()
	return HttpResponse(state.state)