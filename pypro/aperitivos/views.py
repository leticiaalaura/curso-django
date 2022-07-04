from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))

videos_list = [
    Video('motivacao', 'Video Aperitivo: Motivação', 722325795),
    Video('instalacao-windows', 'Instalação Windows', 251497668)
               ]

videos_dict = {v.slug: v for v in videos_list}

videos = {'motivacao': {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 722325795},
          'instalacao-windows': {'slug': 'instalacao-windows', 'titulo': 'Instalação Windows', 'vimeo_id': 251497668}}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos_list})


def video(request, slug):
    video = videos_dict[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

# def video(request, slug):
#     content = videos[slug]
#     return render(request, 'aperitivos/video.html', context={'video': content})
