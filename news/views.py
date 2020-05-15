from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
#A view is a function that takes the request from a user,
#  processes it and returns a response to the user
def welcome(request):
    return HttpResponse('Welcome to the Daily Tribune')  

#function to get news for a particular day.  
def news_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)   
       
#date weekdday function
def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    # Returning the actual day of the week
    day = days[day_number]
    return day   

#passing request to get exact day         
def news_of_day(request):
    date = dt.date.today()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)          

        