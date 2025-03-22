from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Income, Outcome, Bonus  # Import your models
from django.db.models import Sum
from datetime import date
import calendar

def chart(request): # Changed the name of the view to chart
    user = request.user
    today = date.today()
    current_year = today.year

    # --- Monthly Income/Outcome ---
    monthly_data = []
    for month in range(1, 13):
        start_date = date(current_year, month, 1)
        end_date = date(current_year, month, calendar.monthrange(current_year, month)[1])

        # Get income and outcome for the month
        income = Income.objects.filter(user=user, date__range=[start_date, end_date]).aggregate(Sum('amount'))['amount__sum'] or 0
        outcome = Outcome.objects.filter(user=user, date__range=[start_date, end_date]).aggregate(Sum('amount'))['amount__sum'] or 0

        monthly_data.append({
            'month': calendar.month_name[month],  # Get month name
            'income': income,
            'outcome': outcome,
        })

    # --- Lifetime Income/Outcome/Bonus ---
    lifetime_income = Income.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum'] or 0
    lifetime_outcome = Outcome.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum'] or 0
    bonus_income = Bonus.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'monthly_data': monthly_data,  # Pass the combined monthly data
        'lifetime_income': lifetime_income,
        'lifetime_outcome': lifetime_outcome,
        'bonus_income': bonus_income,
        'months': [calendar.month_name[i] for i in range(1, 13)], # For the template
    }
    return render(request, 'chart.html', context)
