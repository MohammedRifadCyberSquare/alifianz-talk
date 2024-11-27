import random
from . models import Participant
def getCode(category):
    letter = random.choice("ABCDE")
    letter_exist = Participant.objects.filter(category=category, code_letter= letter).exists()
    if not letter_exist:
        return letter
    else:
        return getCode(category)

