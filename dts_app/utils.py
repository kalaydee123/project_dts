from .models import *
from project_dts.users.models import User

def get_choices(choice_field):
    start_tuple = ()
    list_tuple = list(start_tuple)

    if choice_field == 'colleges':
        for choice in User.COLLEGE_CHOICES:
            list_tuple.append({'value': choice[0], 'description': choice[1]})

    choices_tuple = tuple(list_tuple)
    print choices_tuple
    return choices_tuple
