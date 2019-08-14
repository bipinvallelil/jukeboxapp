from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MyForm
from .models import Video


def home_view(request, *args, **kwargs): # *args, **kwargs
    return render(request, "slackvideoapp/home.html", {})
# process form data,home page
def home(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = MyForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            k = form.cleaned_data['choice_field']
            vid = Video.objects.get(yt_id=k)
            vid.vote += 1
            vid.save()


            return HttpResponseRedirect('/slackvideoapp/home/')  # Redirect after POST
    else:
        form = MyForm()  # An unbound form

    return render(request, 'slackvideoapp/jukebox.html', {'form': form})


# render youtube embed with list of videoSs
def jukebox(request):
    url_list = Video.objects.all()
    newlist = sorted(url_list, key=lambda x: x.vote, reverse=True)
    k = [x.yt_id for x in newlist]
    first = str(k[0])
    last = ",".join(k[1:])
    context = {'url_list': url_list, 'newlist': newlist, 'first': first, 'last': last}
    return render(request, 'slackvideoapp/index.html', context)


