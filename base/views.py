import math
from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Room, HomeQuestions, Question, Option, CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages





@login_required(login_url='login')
def home(request):
    rooms = Room.objects.all()
    homeQuestions = HomeQuestions.objects.all()
    custom_user = CustomUser.objects.get(id=request.user.id)
    mark = custom_user.mark
    username = request.user.username.capitalize()
    context = {'username': username,'rooms':rooms, 'homeQuestions':homeQuestions, 'mark': mark}
    return render(request, 'home.html', context)



from django.contrib import messages

@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(uid=pk)
    questions = Question.objects.filter(room=room).order_by('created')

    if request.method == 'POST':
        que_list = []
        opt_list = []
        note_list = []
        question_mark = 0
        option_mark = 0
        
        for question in questions:
            option_uid = request.POST.get('q{}'.format(question.uid))
            option = Option.objects.get(uid=option_uid)
            que_list.append(option.question.question)
            opt_list.append(option.option)
            note_list.append(option.note)
            question_mark += option.question.marks
            option_mark += option.mark

        score = math.floor(option_mark / question_mark * 100)

        # Update CustomUser with the score and is_filled=True
        custom_user = CustomUser.objects.get(id=request.user.id)
        custom_user.refresh_from_db()
        custom_user.mark = score
        custom_user.is_filled = True
        custom_user.save()

        # Send messages with question, option, and note values
        for i in range(len(que_list)):
            messages.add_message(request, messages.SUCCESS, f'Question: {que_list[i]}')
            messages.add_message(request, messages.INFO, f'Option You Chose: {opt_list[i]}')
            messages.add_message(request, messages.WARNING, f'Note: {note_list[i]}')

        return redirect('home')

    for question in questions:
        options = Option.objects.filter(question=question).order_by('created')
        question.options = options

    rooms = Room.objects.all()
    custom_user = CustomUser.objects.get(id=request.user.id)
    mark = custom_user.mark
    username = request.user.username.capitalize()
    context = {'username': username, 'room':room, 'questions':questions, 'mark': mark, 'rooms':rooms}
    return render(request, 'room.html', context)


@login_required(login_url='login')
def survey(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)
        custom_user.evaluation = request.POST.get('message')
        custom_user.save()
        messages.success(request, 'Evaluation submitted successfully!')
        return redirect('home')

    rooms = Room.objects.all()
    custom_user = CustomUser.objects.get(id=request.user.id)
    mark = custom_user.mark
    username = request.user.username.capitalize()
    context = {'username': username,'mark': mark, 'rooms':rooms}
    return render(request, 'survey.html', context)



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, 'Your password and confirm password do not match!')
            return redirect('signup')
        else:
            my_user = CustomUser.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')

    return render(request, 'signup.html')
        

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!!!", extra_tags='danger')
            return redirect('login')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
