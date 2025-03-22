from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import transactions
from django.core.paginator import Paginator

# Create your views here.


def transactions_list(request):
    transactionss = transactions.objects.filter(user=request.user).order_by('-date')
    print("Transactions:", transactions)  # Check the queryset
    paginator = Paginator(transactionss, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print("Page object:", page_obj)  # Check the page object
    print("Page object content:", page_obj.object_list) # Check the list of objects in the page
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'transactions.html', context)