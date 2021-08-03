from django.shortcuts import render, redirect, get_object_or_404
from quizapp.models import Answer, Question, Quizzes, Attempt
from quizapp.forms import NewQuizForm, NewQuestionForm


def home(request):
    if request.user.is_authenticated:
        quiz = Quizzes.objects.all()
        context = {
            'quiz': quiz,
        }
        return render(request, "quiz/home.html", context)
    else:
        return redirect("user_login")


def takequiz(request, quiz_id):
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    context = {
        'quiz': quiz,
    }
    return render(request, 'quiz/takequiz.html', context)


def deletequiz(request, quiz_id):
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    quiz.delete()
    return redirect('home')


def submitquiz(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    earned_marks = 0
    score = 0
    if request.method == 'POST':
        questions = request.POST.getlist('question')
        answers = request.POST.getlist('answer')

        for q, a in zip(questions, answers):
            question = Question.objects.get(id=q)
            answer = Answer.objects.get(id=a)
            if answer.is_correct == True:
                earned_marks += question.mark
                score = earned_marks
        attempt = Attempt.objects.create(
            user=user, quiz=quiz, question=question, answer=answer, score=score)
        return redirect('home')


def newquiz(request):
    user = request.user
    if request.method == 'POST':
        form = NewQuizForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            quiz = Quizzes.objects.create(
                user=user, title=title, description=description)
            return redirect('newquestion', quiz_id=quiz.id)
    else:
        form = NewQuizForm()

    context = {
        'form': form,
    }
    return render(request, 'quiz/newquiz.html', context)


def newquestion(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data.get('question_text')
            mark = form.cleaned_data.get('marks')
            answer_text = request.POST.getlist('answer_text')
            is_correct = request.POST.getlist('is_correct')

            question = Question.objects.create(
                question_text=question_text, user=user, mark=mark)

            for a, c in zip(answer_text, is_correct):
                answer = Answer.objects.create(
                    answer_text=a, is_correct=c, user=user)
                question.answers.add(answer)
                question.save()
                quiz.questions.add(question)
                quiz.save()
            return redirect('newquestion', quiz_id=quiz.id)
    else:
        form = NewQuestionForm()

    context = {
        'form': form,
    }
    return render(request, 'quiz/newquestion.html', context)


def results(request):
    user = request.user
    attempt = Attempt.objects.filter(user=user)

    context = {
        'attempt': attempt,
    }
    return render(request, 'quiz/results.html', context)


def report(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quizzes, id=quiz_id)
    attempts = Attempt.objects.filter(quiz=quiz, user=user)

    context = {
        'quiz': quiz,
        'attempts': attempts,

    }
    return render(request, 'quiz/report.html', context)


def aboutme(request):
    return render(request, 'quiz/aboutme.html')
