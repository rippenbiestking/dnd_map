import json

from actual.models import User


def header_middleware(get_response):
    def middleware(request):
        if 'DND-USER-ID' in request.headers:
            request.user = User.objects.get(user_id=request.headers['DND-USER-ID'])

        # TODO: add similar for campaign, and others as needed

        return get_response(request)
    
    return middleware
