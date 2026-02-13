
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
  'january': '100',
  'february': '250',
  'march': '50',
  'april': '104',
  'may': '105',
  'june': '106',
  'july': '107',
  'august': '108',
  'september': '109',
  'october': '110',
  'november': '111',
  'december': '112'
}

def monthlynumber_challenge(request, month):

  months = list(monthly_challenges.keys())
  if (month)>len(months):
    return HttpResponseNotFound("<h1>No such month exists</h1>")
  forward_months = months[month-1]
  forward_url = reverse("challenges-monthly", args=[forward_months])
  return HttpResponseRedirect(forward_url)
def monthly_challenge(request, month):
  try:
   message = monthly_challenges[month]
   return render(request, "challenges/challenges.html", {"text": message, "text2": month.capitalize()})
  except:
    return HttpResponseNotFound("No such month exists")
  # return HttpResponse(f"<h1>{message}</h1>")
def index(request):
  month_data = ""
  months = list(monthly_challenges.keys())
  for month in months:
     print(month)
     url_name = reverse("challenges-monthly", args=[month])
     month_data += f"<li><a href= \"{url_name}\">{month}</a></li>"
  print(month_data)
  results = f"<ul>{month_data}</ul>"
  return HttpResponse(results)