from django.conf import settings


def check(request):
    kwargs = {
        'user': request.user.is_authenticated
    }
    return kwargs
