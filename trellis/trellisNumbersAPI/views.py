from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services import num_to_english
import json



@csrf_exempt
def get_num_to_english(request):
    try:
        number = None
        if request.method == 'GET':
            number = int(request.GET.get('number'))
            print(number)
        elif request.method == 'POST':
            number = json.loads(request.body).get('number')

        if len(str(number)) > 102:
            raise ValueError('Number is too large')

        num_in_english = num_to_english(number)
        return JsonResponse({'status': 'ok', 'num_in_english': num_in_english})
        
    except (ValueError, TypeError) as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': 'Invalid number'}, status=500)
        

