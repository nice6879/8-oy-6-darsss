from django.shortcuts import render
from models import Quiz


def quizList(request):
    quizList = Quiz.objects.all()
    return render(request, 'quizlist.html', {'quizList': quizList})



def quizDetail(request,id):
    quiz = Quiz.objects.get(Quiz,id)
    return render(request, 'quizdetail.html', {'quizDetail': quiz})


def quizCreate(request):
    if request.method == 'POST':
        quiz = Quiz.objects.create(
            name=request.POST.get['name'],
            author=request.POST.get['author'],
            amount=request.POST.get['amount']

        )

        return render(request, 'quizcreate.html', {'quizCreate': quiz})


def quizUpdate(request,id):
    if request.method == 'POST':
        quiz = Quiz.objects.get(id=id)
        name = request.POST.get('name')
        author = request.POST.get('author')
        amount = request.POST.get('amount')

        quiz.name = name
        quiz.author = author
        quiz.amount = amount

        quiz.save()
        return render(request, 'quizupdate.html', {'quizUpdate': quiz})







