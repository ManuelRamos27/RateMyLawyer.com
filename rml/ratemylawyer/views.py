from django.shortcuts import render

# Create your views here.

def ratemylawyer(request):
    if request.method == 'GET':
        return render(request = request,
                    template_name = 'main.html')
def main(request):
    return render(request, 'main.html')
     
