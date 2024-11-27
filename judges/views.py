from django.shortcuts import render,redirect
from alif_admin.models import *

# Create your views here.

def dashboard(request):
    if request.method == 'POST':
        category = request.POST['category']
        records = Score.objects.filter(judge = request.session['judge_id'], student__category = category)

        return render(request,'judges/MyMarks.html',{'records': records,'category':category})
    return render(request,'judges/MyMarks.html')


def participant_list(request):
    no_data = False
    if request.method == 'POST':
        category = request.POST['category']

        participants = Participant.objects.filter(category = category)
        if not participants:
            no_data = True
        return render(request,'judges/ParticipantsList.html', {'participants':participants,'category':category,'no_data': no_data})

    return render(request,'judges/ParticipantsList.html')

def mark(request,id):
    selected_participant = Participant.objects.get(id = id)
    selected_category = selected_participant.category
    message = ''
    code_letter = selected_participant.code_letter 
    if request.method == 'POST':
        content = request.POST['content']
        presentation_skills = request.POST['presentation_skills']
        confidence = request.POST['confidence']
        cohesion = request.POST['cohesion']
        grammar = request.POST['grammar']
        pronounce = request.POST['pronounce']
        voice = request.POST['voice']
        comment = request.POST['comment'].strip()
        total = float(content) + \
                float(presentation_skills) + \
                float(confidence) + \
                float(cohesion) + \
                float(grammar) + \
                float(pronounce) + \
                float(voice)
        participant_record = Score.objects.filter(student = id, judge_id = request.session['judge_id'])
        print(request.session['judge_id'],'**')
        if not participant_record:
            print(request.session['judge_id'],'**')

            record = Score(
                student_id = id,
                rubrics1 = content,
                rubrics2 = presentation_skills,
                rubrics3 = confidence,
                rubrics4 = cohesion,
                rubrics5 = grammar,
                rubrics6 = pronounce,
                rubrics7 = voice,
                comments = comment,
                judge_id = request.session['judge_id'],
                total = total
            )

            record.save()
            message = 'Score Added Succesfully'

        else:
            print('else working..')
            participant_record[0].rubrics1 = content
            participant_record[0].rubrics2 = presentation_skills
            participant_record[0].rubrics3 = confidence
            participant_record[0].rubrics4 = cohesion
            participant_record[0].rubrics5 = grammar
            participant_record[0].rubrics6 = pronounce
            participant_record[0].rubrics7 = voice
            participant_record[0].comments = comment
            participant_record[0].total = total

            participant_record[0].save()

            message = 'Score Updated Succesfully'






    return render(request,'judges/Mark.html',{'selected_category': selected_category, 'code_letter': code_letter, 'message': message} )
    

def logout(request):
    del request.session['judge_id']
    del request.session['judge_name']
    request.session.flush()
    return redirect('common:admin_login')

def my_marks(request):
    print(request.session['judge_id'],'8888888888')
   

    return render(request,'judges/MyMarks.html')
