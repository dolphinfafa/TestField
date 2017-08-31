from django.shortcuts import render

from jingpai.models import Event

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    event_list = Event.objects.order_by('-event_date')

    print event_list

    context_dict= {'events': event_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'jingpai/index.html', context_dict)
