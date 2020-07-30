from django.http import HttpResponse

def index(request):
    return HttpResponse("DJango project")

def home(request):
    return HttpResponse("<h1 style='color:blue'>Hello welcome to difficult but easy task</h1>")


#localhost/name/age
#localhost/simran/15 --> simran cannot vote
#localhost/survi/20 --> survi can vote