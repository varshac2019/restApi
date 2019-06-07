import psycopg2
import requests
import json
import re 
import urllib.request 
from bs4 import BeautifulSoup
from university.models import  University,ProgramHighlight


def test():
    conn = psycopg2.connect(database="links", user = "postgres", password = "varsha03", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT  name from university_university")
    rows = cur.fetchall()
    title="Pune"
    url="www.Pune.com"
    rank_display = 1
    country = "India"
    city ="Pune"

    insert_query='''insert into university_university values(%s,%s,%s,%s,%s,%s)'''
    cur.execute(insert_query,(id,rank_display,title,city,country,url))
    conn.commit()
    



def get_data_from_link(link,id):
    conn = psycopg2.connect(database="links", user = "postgres", password = "varsha03", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    
    delete_query ='''delete from university_programhighlight'''
    cur.execute(delete_query)
    conn.commit()

    delete_query ='''delete from university_university'''
    cur.execute(delete_query)
    conn.commit()
    
    LINK = "https://www.topmba.com"

    raw = requests.get(link).text
    data_dict = json.loads(raw)

    for key, value in data_dict.items():
        break

    i = 0
    while i!=len(data_dict[key]): 
        clean        = re.compile('<.*?>')                                       #remove tags from   title
        title        = re.sub(clean, '', data_dict[key][i].get('title'))         #data_dict[key][i].get('title') 
        url          = data_dict[key][i].get('url')
        rank_display = data_dict[key][i].get('rank_display')
        country      = data_dict[key][i].get('country')
        city         = data_dict[key][i].get('cities')           
    
    
        try:
            response = urllib.request.urlopen(LINK+url)

        except:
            print(LINK+url+" Not Working")

        soup = BeautifulSoup(response, 'html.parser')
        highlights = soup.find('div',class_='directory-data') 

        start_month = class_size = avg_work_exp = avg_stud_age = intl_stud = women_stud = avg_salary = scholarship = accreditions = employed = "NULL"

        if highlights!=None:
            lst =[]
            for string in highlights.stripped_strings:
                lst +=[str(string)]

     
            try:
                start_month = lst[lst.index('Start Month')+1]       
            except:
                start_month = "NULL"
                print('Start Month Not present in list')

            try:
                class_size = lst[lst.index('Class Size')+1]       
            except:
                class_size = "NULL"       
                print('Class Size Not present in list')

            try:
                avg_work_exp = lst[lst.index('Avg. Work Experience')+1]       
            except:
                avg_work_exp = "NULL"       
                print('Avg work exp Not present in list')

            try:
                avg_stud_age = lst[lst.index('Avg. Student Age')+1]       
            except:
                avg_stud_age = "NULL"       
                print('Avg stud age Not present in list')

            try:
                 intl_stud= lst[lst.index("Int'l Students")+1]       
            except:
                 intl_stud= "NULL"       
                 print("Int'l Students Not present in list")

            try:
                 women_stud= lst[lst.index('Women Students')+1]       
            except:
                 women_stud="NULL"    
                 print('Women Students Not present in list')

            try:
                 avg_salary= lst[lst.index('Avg. Salary(Post 3 Months)')+1]       
            except:
                 avg_salary= "NULL"       
                 print('Avg salary Not present in list')

            try:
                 scholarship = lst[lst.index('Scholarship')+1]       
            except:
                 scholarship = "NULL"      
                 print('Scholarship Not present in list')

            try:
                accreditions = lst[lst.index('Accreditations')+1]       
            except:
                accreditions = "NULL"
                print('Accreditations Not present in list')

            try:
                employed = lst[lst.index('Employed(Post 3 Months)')+1]
            except:
                employed = "NULL"
                print('Employed(Post 3 Months) Not present in list')

 
        
        University.objects.create(rank_display,title,city,country,LINK+url)
        ProgramHighlight.objects.create(start_month,class_size,avg_work_exp,avg_stud_age,intl_stud,women_stud,avg_salary,scholarship,accreditions,id,employed)
#        insert_query='''insert into university_university values(%s,%s,%s,%s,%s,%s)'''
#        cur.execute(insert_query,(id,rank_display,title,city,country,LINK+url))
#        conn.commit()
        
#        insert_query='''insert into university_programhighlight values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
#        cur.execute(insert_query,(id,start_month,class_size,avg_work_exp,avg_stud_age,intl_stud,women_stud,avg_salary,scholarship,accreditions,id,employed))
#        conn.commit()

        id+=1
        i+=1 


    
def main():
    link = "https://www.topmba.com/sites/default/files/qs-rankings-data/330380.txt?_=1559710076340"
    id=1
    get_data_from_link(link,id)
    


if __name__== "__main__":
  main()


