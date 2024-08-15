# views.py (Django)
from django.http import JsonResponse
from .models import Namespace  # type: ignore # Import the Namespace model

def connect_to_blazegraph(request):
    # Connect to BlazeGraph logic
    return JsonResponse({"message": "Connected to BlazeGraph"})

def create_database(request):
    github_link = 'https://github.com/blazegraph'  # Using the BlazeGraph GitHub link
    # Create database from GitHub link logic
    return JsonResponse({"message": "Database created from GitHub link"})

def add_namespace(request):
    namespace_name = request.POST.get('namespace')
    new_namespace = Namespace(name=namespace_name)
    new_namespace.save()
    return JsonResponse({"message": f"Added new namespace: {namespace_name}"})