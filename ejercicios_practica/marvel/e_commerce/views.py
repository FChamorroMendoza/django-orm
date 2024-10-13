# Create your views here.
from django.http import JsonResponse
from e_commerce.models import Comic


def comic_list_api_view(request):
    if request.method == 'GET':
        try:
            comics = Comic.objects.all()
            comics_data = list(comics.values())
            return JsonResponse(comics_data, safe=False)  # Cambia a safe=False para permitir listas
        except Exception as e:
            return JsonResponse(data={"message": "Error al obtener cómics.", "error": str(e)}, status=500)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)

def comic_filter_stock_api_view(request):
    if request.method == 'GET':
        try:
            filtered_comics = Comic.objects.filter(stock_qty=5)
            filtered_comics_data = list(filtered_comics.values())
            return JsonResponse(filtered_comics_data, safe=False)  # Cambia a safe=False
        except Exception as e:
            return JsonResponse(data={"message": "Error al filtrar cómics.", "error": str(e)}, status=500)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_filter_price_api_view(request):
    if request.method == 'GET':
        try:
            filtered_comics = Comic.objects.filter(price__gt=3)
            filtered_comics_data = list(filtered_comics.values())
            return JsonResponse(filtered_comics_data, safe=False)  # Cambia a safe=False
        except Exception as e:
            return JsonResponse(data={"message": "Error al filtrar cómics.", "error": str(e)}, status=500)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)

def comic_list_order_api_view(request):
    if request.method == 'GET':
        try:
            ordered_comics = Comic.objects.all().order_by('marvel_id')
            ordered_comics_data = list(ordered_comics.values())
            return JsonResponse(ordered_comics_data, safe=False)  # Cambia a safe=False
        except Exception as e:
            return JsonResponse(data={"message": "Error al obtener cómics ordenados.", "error": str(e)}, status=500)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)