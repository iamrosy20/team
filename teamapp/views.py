from django.shortcuts import render

# Create your views here.

def team(request):
    return render(request, "team.html")

def result(request):
    userinput = int(request.GET['input'])
    if userinput == 3:
        output = "우리는 3팀!"
    else:
        output = "틀렸습니다."
    return render(request, "result.html", {'output' : output})
    