import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Board_member, Feedback

def index(request):
    board = Board_member.objects.all()
    return render(request,'contact/contact.html',{"board":board})

@csrf_exempt
def feedback(request):
        if request.method == "POST":
                try:
                        data  = json.loads(request.body.decode('utf-8'))
                        feedback = Feedback.objects.create(name=data['form'].get("name", ""),
                                                                                                        email = data['form'].get("email", ""),
                                                                                                        message=data['form'].get("message", "") )
                        response_data = {"message":"message received"}
                        return HttpResponse(
                                json.dumps(response_data),
                                content_type="application/json")
                except:
                        response_data = {"message":"something went wrong"}
                        return HttpResponse(
                                json.dumps(response_data),
                                content_type="application/json")
        else:
                return HttpResponse(
                        json.dumps({"nothing to see": "this isn't happening"}),
                        content_type="application/json"
                        )

                                                                