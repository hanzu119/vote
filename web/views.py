from django.shortcuts import render


# Create your views here.
def test(request):
    print("heihei")
    return render(request, "my_vote.html")
