from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    context = {}
    return render_to_response('game_home.html', context, context_instance=RequestContext(request))