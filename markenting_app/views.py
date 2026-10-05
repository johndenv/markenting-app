from django.shortcuts import render
from django.views import View
from yt_dlp import YoutubeDL

class ExtractionView(View):
    template_name = "markenting_app/extraction.html"

    def get(self, request, *args, **kwargs):
        
        # retorna minha pagina html
        return render(request, self.template_name)

    def push(self):
        pass




