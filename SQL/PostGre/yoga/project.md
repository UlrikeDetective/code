Front and Back end yoga studio / lessons with postgres

front end: studends can book solo yoga lessons or yoga packages

back end: the business - customers: residents/locals and vistors. paid classes, paid packages - if package - how many lessons left, buying materials (yoga mats and co), other costs - like car / gas, going on holiday, how much is the income per week / month / year, small adds (instagram and co)

Scenario: Side Job - giving almost daily morning yoga lessons on the beach (beach = free) in Tarifa. If the weather is good there are six yoga lessons per week monday to saturday between 9am - 10am. Occationaly there is an extra lesson on sunday or in the afternoon. At a yoga lessons there should be at least 3 students with a maximum of 20. Some of the customers are local residents who drop by more or less regulary (mostly once per week) and vistors, who stay a few days to two weeks in Tarifa. Some vistors come every year (or more than once a year), some vistors only come once or not that often. I do advertising (blackboards) at surf schools, cafes ect and on Instagram. For the lessons I need to provide my students yoga mats. The lifetime of a daily used yoga mat on the beach is 1 to 2 years. 

The price of yoga mats: 10 mats for 31,33 Euros a piece, 20 mats for 31,05 Euros a piece, 30 mats for 29,33 Euros a piece

Costs of Yoga lessons: single lesson: 15 Euros, 3 lessons: 40 Euros, 5 classes 50 Euros, 10 classes 100 Euros

my costs: yoga mats, gas, car, advertising (blackboards, instagram, co), taxes
income: paid yoga classes

Please help me build a front end for booking yoga lessons and packages, a back end for my business and business plan

use: postgres, .env, django?, conda

conda run -n django python manage.py runserver



python manage.py runserver
python-dotenv could not parse statement starting at line 8
python-dotenv could not parse statement starting at line 10
python-dotenv could not parse statement starting at line 11
python-dotenv could not parse statement starting at line 8
python-dotenv could not parse statement starting at line 10
python-dotenv could not parse statement starting at line 11
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 04, 2026 - 10:01:06
Django version 6.0.2, using settings 'yoga_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/

Build a Business Plan
Add to the calendar behind the yoga session how many spots / places are booked - checked
When booking a yoga session / package - please keep the customer "logged in" until the customer logs out. Thats easier with booking classes. - checked
When logged in, please show the customer which classes they have already booked in the calendar. - checked
In the owners dashboard, please show the customers from Tarifa, which last booked clase is less than one week away.