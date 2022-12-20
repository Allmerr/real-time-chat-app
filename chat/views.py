from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from chat.models import room as room_model
from chat.models import message as message_model


# Create your views here.

def home(request):
    return render(request, 'home.html')

def checkRoom(requsest):
    room_name = requsest.POST['room_name']
    username = requsest.POST['username']

    if room_model.objects.filter(name=room_name).exists():
        return redirect('/' + room_name + '/?username=' + username)
    else :
        new_room = room_model.objects.create(name=room_name)
        new_room.save()
        return redirect('/' + room_name + '/?username=' + username)


def room(request, room):
    room_data = room_model.objects.get(name=room)
    username = request.GET.get('username')
    konteks = {
        'room_data' : room_data,
        'room_name' : room,
        'username' : username
    }

    return render(request, 'room.html', konteks)

def send(request):
    username = request.POST['username']
    id_room = request.POST['id_room']
    value_message = request.POST['value_message']

    new_message = message_model.objects.create(value=value_message,user=username,room=id_room)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = room_model.objects.get(name=room)
    messages = message_model.objects.filter(room=room_details.id)

    return JsonResponse({"messages":list(messages.values())})
