from django.shortcuts import render , redirect
from django.contrib.auth.models import auth , User
from .models import *
# Create your views here.
def home(request):
    msg = ''
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user_id = User.objects.create_user(username=username, password=password)
        user_id.save()
        user_id1 = user_id.id
        UserRole.objects.create(user_id=user_id1,role_id=role)
        msg = 'User created successfully'
        return render(request, 'home.html',{'msg':msg})

    else:
        return render(request, 'home.html',{'msg':msg})

def login(request):
  
    if request.method=='POST': 
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = auth.authenticate(username=username , password = password)
        if user is not None :
            auth.login(request, user)
            
            x=UserRole.objects.filter(user_id=user.id).exists()
            if x :
                x1=UserRole.objects.get(user_id =user.id).role_id
                if x1 == 1 :
                    return redirect('/student')
                elif x1 == 2:
                    return redirect('/mentor')
                else:
                    return redirect('/')
            else:
                return redirect('/')
        else:
            return redirect('login')

    else:
        
        return render(request , 'login.html')    

def logout(request):
    auth.logout(request)
    return redirect('/')        

def student(request):
    msg = ''
    status=''
    user_id = request.user.id
    if request.method=='POST':
        purpose = request.POST.get('purpose')
        startdate = request.POST.get('starting')
        enddate = request.POST.get('ending')
        duration = request.POST.get('duration')
        
        status = 'pending'
        Leave.objects.create(purpose= purpose , start_date= startdate , end_date= enddate , duration = duration , student_id=user_id,status=status , comment='' )
        msg = 'Applied successfully'
    
    leaveCheck = Leave.objects.filter(student_id=user_id).exists()
    leaveCheckFlag = 0
    leaveCheckValue = []
    if leaveCheck:
        leaveCheckValue = Leave.objects.filter(student_id=user_id)
        leaveCheckFlag =1
    
    return render(request, 'student.html',{'msg':msg, 'leavecheckvalue':leaveCheckValue,'leavecheckflag':leaveCheckFlag})
   

def mentor(request):
    user_id = request.user.id
    check = MenStu.objects.filter(mentor_id=user_id).exists()
    getAllStudentList = []
    getAllstudentInfo = []
    flag = 0
    
    if request.method == 'POST':
        status1 = request.POST.get('statusbtn')
        rowid = request.POST.get('rowid')
        comment1=request.POST.get('comment')
        #print(status1)
        updateObj =  Leave.objects.get(id=rowid )
        updateObj.status = status1
        updateObj.comment = comment1
        updateObj.save()
    
    if check:
        getAllStudent = MenStu.objects.filter(mentor_id=user_id)
        for getvalue in getAllStudent:
            getAllStudentList.append(getvalue.student_id)
    if len(getAllStudentList) > 0:
        check1 = Leave.objects.filter(student_id__in=getAllStudentList).exists()
        if check1:
            flag =1
            getAllstudentInfo =  Leave.objects.filter(student_id__in=getAllStudentList)
    return render(request, 'mentor.html',{'getAllstudentInfo':getAllstudentInfo,'flag':flag})