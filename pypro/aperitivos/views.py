from django.shortcuts import render

from pypro.aperitivos.models import Video

videos_list = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='722325795'),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id='251497668'),
               ]

videos_dict = {v.slug: v for v in videos_list}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos_list})


def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})

