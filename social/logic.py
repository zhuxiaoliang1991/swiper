from user.models import User
import datetime


def get_rcmd_user(user):
    sex = user.profile.dating_sex
    location = user.profile.location
    min_age = user.profile.min_dating_age
    max_age = user.profile.max_dating_age

    current_year = datetime.date.today().year
    min_year = current_year - max_age
    max_year = current_year - min_age
    users = User.objects.filter(sex=sex,location=location,birth_year__gte=min_year,birth_year__lte=max_year)


    return users
