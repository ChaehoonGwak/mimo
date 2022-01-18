from django.shortcuts import render

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

from mimoapp.mimo import Mimo


# Create your views here.
def home(request):
    return render(request, 'home.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
mimo = Mimo()

@gzip.gzip_page
def mimo_video(request):
    try:
        mimo.create()
        return StreamingHttpResponse(gen(mimo), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass