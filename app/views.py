from django.http import HttpResponse
from app.models import State

def index(request):

    return HttpResponse(State.objects.first().state)


def post(request, newState):
	state = State.objects.first()
	state.state = newState
	state.save()
	return HttpResponse(state.state)