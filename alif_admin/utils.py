import random
from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from . models import Participant
def getCode(category):
    letter = random.choice("ABCDEFGHIJ")
    letter_exist = Participant.objects.filter(category=category, code_letter= letter).exists()
    if not letter_exist:
        return letter
    else:
        return getCode(category)

def render_to_pdf(template_src, context_dict={}):
    template = render(None, template_src, context_dict)
    html = template.content.decode('utf-8')
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None