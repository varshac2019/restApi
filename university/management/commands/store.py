import requests
import json
import re 
import urllib.request 
from bs4 import BeautifulSoup
from university.models import University,ProgramHighlight    
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help ='store data in database'
    def handle(self, *args, **options):
        LINK = "https://www.topmba.com"
        MAIN_LINK = "https://www.topmba.com/sites/default/files/qs-rankings-data/330380.txt?_=1559710076340"

        raw = requests.get(MAIN_LINK).text
        data_dict = json.loads(raw)

        for key, value in data_dict.items():
            for item in value:
                university_dict = {}
                clean = re.compile('<.*?>')                                                         
                university_dict['name'] = re.sub(clean, '', item['title'])
                university_dict['link_to_program'] = LINK+item['url']
                university_dict['rank'] = item['rank_display']
                university_dict['location'] = item['country']
                university_dict['city'] = item['cities']
        
                try:
                    response = urllib.request.urlopen(LINK+item['url'])

                except:
                    print(LINK+item['url']+" <--- Not Working")

                soup = BeautifulSoup(response, 'html.parser')
                highlights = soup.find('div',class_='directory-data')


                if highlights!=None:
                    lst = highlights.text.split('\n')
                    prog_highlight = [value for value in lst if value != '']

                    dictionary = {}
                    key_index = 0
                    for string in prog_highlight:
                        if key_index%2==0:
                            new_key = string.replace(' ','_').lower()
                        else:
                            dictionary[new_key] = string
                        key_index+=1


                    if "int'l_students" in dictionary.keys():
                        dictionary["intl_students"]=dictionary.pop("int'l_students")
    
                    if "avg._salary(post_3_months)" in dictionary.keys():
                        dictionary["avg_salary"]=dictionary.pop("avg._salary(post_3_months)")

                    if "employed(post_3_months)" in dictionary.keys():
                        dictionary["employed"]=dictionary.pop("employed(post_3_months)")

                    if "avg._student_age" in dictionary.keys():
                        dictionary["avg_student_age"]=dictionary.pop("avg._student_age")
    
                    if "avg._work_experience" in dictionary.keys():
                        dictionary["avg_work_experience"]=dictionary.pop("avg._work_experience")
        
                    obj_uni = University.objects.create(**university_dict)
                    dictionary.update({'name':obj_uni})
                    obj_prog = ProgramHighlight.objects.create(**dictionary)
