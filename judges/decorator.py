from django.shortcuts import redirect
from functools import wraps

def auth_judge(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the session variable exists
        if 'judge_id' not in request.session:
            # Redirect to login page or any other page
            return redirect('common:admin_login')  # Change 'login' to your actual login URL name
        return view_func(request, *args, **kwargs)
    return _wrapped_view
