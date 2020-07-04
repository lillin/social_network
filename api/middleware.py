from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


class UpdateLastUserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            try:
                request.user.last_activity = timezone.now()
                request.user.save()
            except ObjectDoesNotExist:
                return
