from django.shortcuts import render, get_object_or_404

from interns.models import Intern


def intern_list(request):
    interns = Intern.objects.all()
    return render(request, 'intern_list.html', {"interns": interns})

def intern_detail(request, id):
    intern = get_object_or_404(Intern, id=id)
    return render(request, 'intern_detail.html', {"intern": intern})