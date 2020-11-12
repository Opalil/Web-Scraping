from django.core.management.base import BaseCommand

import requests
from bs4 import BeautifulSoup
import json

from app.models import Job

class Command(BaseCommand):

    def handle(self, *args, **options):

        #html_base = urlopen('https://www.monster.fi') # Base url for jobs
        #html_loc = '/tyopaikat/haku/?where=kuopio' # Location param
        
        html_url = ('https://www.monster.fi/tyopaikat/haku/?where=kuopio')  #html_base + html_loc # Merge url 
        page = requests.get(html_url)
        bSoup = BeautifulSoup(page.content, 'html.parser')

        job_container = bSoup.find(id='ResultsContainer')
        # Get job postings 
        jobs = job_container.find_all('section', class_='card-content')
        
        for job in jobs:
            url = job.find('a')
            title = job.find('h2', class_='title')
            location = job.find('div', class_='location')
            description = job.find('div', class_='details-content')
            if None in(url, title, location, description):
                continue
            # Check
            href_url = url.get('href')
            if href_url is None:
                continue
            
            #tUrl = url.text
            tTitle = title.text
            tLocation = location.text
            tDescription = description.text

            try:
                Job.objects.create(
                    url = href_url,
                    title = tTitle,
                    location = tLocation,
                    description = tDescription
                )
                print('%s added ' % (title,))
            except:
                print('%s already exists in database' % (title,))

            self.stdout.write('Done')