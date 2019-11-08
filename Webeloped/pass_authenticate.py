from django.conf import settings


def check(request):
    kwargs = {
        'user_auth': request.user.is_authenticated
    }
    return kwargs
