
import requests
import json

def Moliere(phrase,l_Nerror_v,l_Showerror_v,l_error_v,l_Pcorrection_v,l_correction_v,l_grade):    
    l_correction_v['text'] = ""
    error = ""
    grade = 100
    t_1 = phrase.replace(" ","+")
    print(t_1)
    response = requests.get(f"https://api.textgears.com/grammar?text={t_1}%3F&language=fr-FR&whitelist=&dictionary_id=&key=9LGT5o8q35HwTt5R")
    y = json.loads(response.text)
        
    l_Nerror_v['text'] ="Nombre d'érreur : " + str(len(y['response']['errors']))
            
    if len(y['response']['errors']) > 0:
        l_Showerror_v['text'] ="Les erreurs sont :"
            
        for x in range(len(y['response']['errors'])) :
            grade -= 1
            error = f"{error},{y['response']['errors'][x]['bad']}"
                
        l_error_v['text'] = error   
        l_Pcorrection_v['text'] ="Correction possible :"
            
        correction = ""

        for x in range(len(y['response']['errors'])) :
            for z in range(len(y['response']['errors'][x]['better'])):
                correction = correction + y['response']['errors'][x]['better'][z] + ", "
                
            l_correction_v['text'] =f"{l_correction_v['text']}{correction} \n"
            correction = ""
        l_grade['text'] =f"{grade}"
    else :
        l_error_v['text'] = "Pas d'erreurs"  
        l_Pcorrection_v['text'] ="Correction possible :"
        l_correction_v['text'] = "Aucune"
        l_grade['text'] =f"{grade}"
            
    print("\n")