from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services import num_to_english
import json



@csrf_exempt
def get_num_to_english(request):
    try:
        payload = None
        if request.method == 'GET':
            payload = request.GET.get('number')
        elif request.method == 'POST':
            payload = json.loads(request.body).get('number')

        number = int(payload)

        if len(str(number)) > 102:
            raise ValueError('Number is too large')
        num_in_english = num_to_english(number)
        return JsonResponse({'status': 'ok', 'num_in_english': num_in_english})
        
    except (ValueError, TypeError) as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': 'Invalid number', 'num_in_english': ''}, status=500)
        

