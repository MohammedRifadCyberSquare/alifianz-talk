from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
import random
from . import utils
from django.views.decorators.csrf import csrf_exempt


def dashboard(request):
    return render(request,'alif_admin/dashboard.html')



def register_student(request):
    message = ''
    if request.method == 'POST':
        participant_name = request.POST['participant_name'].lower()
        admission_no = request.POST['admission_no']
        student_cls = request.POST['student_cls']
        division = request.POST['division']
        category = request.POST['category']



        record = Participant.objects.filter(admission_no = admission_no)

        if not record:
            _ = Participant(
                        student_name = participant_name, 
                        admission_no=admission_no,
                         student_cls=student_cls,
                         division=division,
                         category = category
                         ).save()
            message = 'Student Added Succesfully '

        else:
            message = 'Admission No Exist'

    return render(request,'alif_admin/registerStudent.html', {'message': message})



def generate_code_letter(request):
    if request.method == 'POST':
        category = request.POST['category']
        participants = Participant.objects.filter(category = category)
        return render(request,'alif_admin/generateCodeLetter.html', {'participants':participants,'category':category})

    return render(request,'alif_admin/generateCodeLetter.html')

@csrf_exempt
def get_code(request):
    participant = Participant.objects.get(id = request.POST['participantId'])

    if participant.code_letter == "":
        code = utils.getCode(request.POST['category'])
        print(code)
        participant.code_letter = code
        participant.save()

    else:
        code = 'Code Letter Already Generated'

    return JsonResponse({'letter': code})