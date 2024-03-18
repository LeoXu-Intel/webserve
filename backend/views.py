from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

def test_view(request):
        number1 = request.GET.get('number1')
        number2 = request.GET.get('number2')

        if number1 is not None and number2 is not None:
            try:
                number1 = int(number1)
                number2 = int(number2)
                result = number1 + number2
                return JsonResponse({'result': result})
            except ValueError:
                return JsonResponse({'error': 'Invalid input'}, status=400)

        return JsonResponse({'error': 'Missing parameters'}, status=400)