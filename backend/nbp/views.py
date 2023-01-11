from django.shortcuts import (HttpResponse)
from django.http import JsonResponse
from nbp.helpers.statistical_measures import median, dominant, standard_deviation, coefficient_of_variation

# Create your views here.
def index(request):
    test = [181, 187, 196, 196, 198, 203, 207, 211, 215, 123, 199]
    result = []
    result.append(median(test))
    result.append(dominant(test))
    result.append(standard_deviation(test))
    result.append(coefficient_of_variation(test))
    
    return JsonResponse(result)