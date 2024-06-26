from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tasks.models import Task
from tasks.serializers import TaskSerializer
# Create your views here.


# on va créer une vue simple
def onetask(request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'tasks/detail.html', {'task': task})


def index(request, pk=None, status=None):
    if pk is not None: # verifi si l'id est founit dans l'url
        task = Task.objects.filter(id=pk)
        task.update(status=status)
        return redirect('index')  # Redirige vers la même vue pour rafraîchir la liste des tâches
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})



@csrf_exempt
def task_list(request):
    """
    List all code tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def task_detail(request, pk):
    """
    Retrieve, update or delete a code task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)
