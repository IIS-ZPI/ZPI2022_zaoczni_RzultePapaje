from django.shortcuts import (HttpResponse)
from django.http import JsonResponse
from nbp.helpers.statistical_measures import median, dominant, standard_deviation, coefficient_of_variation
from datetime import datetime, timedelta
from nbp.models import TabelaA
# Create your views here.

def measures(request):

    if request.method == 'GET':
        currency = request.GET.get('currency', '')
        time_intervals = [7, 14, 30, 90, 180, 360]
        results = []
        data_array = []
        #  get the latest date from the database
        date_str = TabelaA.objects.all().order_by("-effective_date")[:1]
        # first_date = datetime.strptime(data_str[0].effective_date, "%Y-%m-%d")
        first_date = date_str[0].effective_date
        
        for time in time_intervals:
            second_date = (first_date-timedelta(days=time))
            query = TabelaA.objects.values_list('mid').filter(code=currency).filter(effective_date__gte = second_date, effective_date__lt = first_date)
            for q in query:
                data_array.append(float(q[0]))
            temp = {
                time : {
                    'medan' : median(data_array),
                    'dominant' : dominant(data_array),
                    'standard_deviation' : standard_deviation(data_array),
                    'coefficient_of_variation' : coefficient_of_variation(data_array),
                }
            }
            results.append(temp)
 
    
    return JsonResponse(results, safe=False)