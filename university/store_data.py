import psycopg2
import requests
import json
import re 
import urllib.request 
from bs4 import BeautifulSoup
#from .models import University,ProgramHighlight

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
        university_dict = {}
        
        clean        = re.compile('<.*?>')                                                          #remove tags from   title
        university_dict['title']        = re.sub(clean, '', data_dict[key][i].get('title'))         #data_dict[key][i].get('title') 
        university_dict['url']          = data_dict[key][i].get('url')
        university_dict['rank_display'] = data_dict[key][i].get('rank_display')
        university_dict['country']      = data_dict[key][i].get('country')
        university_dict['city']         = data_dict[key][i].get('cities')           
    
        print(university_dict)        

        try:
            response = urllib.request.urlopen(LINK+data_dict[key][i].get('url'))

        except:
            print(LINK+data_dict[key][i].get('url')+" Not Working")

        soup = BeautifulSoup(response, 'html.parser')
        highlights = soup.find('div',class_='directory-data') 


        if highlights!=None:
            lst = highlights.text.split('\n')
            prog_highlight = [value for value in lst if value != '']

            j=0
            k=0
            dictionary={}
            for string in prog_highlight:
                if j%2==0:
                    l=""
                    splt = string.split(" ")
                    k=0
                    while k!=len(splt):
                        l+=splt[k].lower()
                        if k!=len(splt)-1:
                           l+="_"
                        k+=1
                else:
                    dictionary[l]=string
                j+=1
        
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
            
            print(dictionary)            

        i+=1 
        id+=1
        
        
    
def main():
    link = "https://www.topmba.com/sites/default/files/qs-rankings-data/330380.txt?_=1559710076340"
    id=1
    get_data_from_link(link,id)
    


if __name__== "__main__":
  main()



