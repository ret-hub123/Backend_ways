from django.http import HttpResponse
from django.shortcuts import render, redirect



def main(request):
    return render(request, 'site_for_notes_apllication/main.html')


def years(request, year):
    if int(year) < 2024:
        return HttpResponse(f'Note for {year}')
    else:
        return redirect('home')
