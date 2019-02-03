from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Render that in the index template
    return render(request, "index.html")


from django.shortcuts import render

# Create your views here.
