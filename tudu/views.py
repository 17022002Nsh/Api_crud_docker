from rest_framework.decorators import api_view
from rest_framework.response import Response

from tudu.models import Todo



@api_view(["POST"])
def tudu_create_api(request):
    data = request.data 
    title = data.get("title")
    description = data.get("description")
    
    todo = Todo.objects.create(title=title, description=description)
    return Response({
        "status" : True,
        "massage" : 'New todo create',  
        "data" : {
            "id" : todo.id,
            "title" : todo.title,
            "description" : todo.description
        }
    })


