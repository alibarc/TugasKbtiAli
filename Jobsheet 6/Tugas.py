ada_family = { 'Rofi': ['Anik', 'Lies','Fendi'],
              'Setya': ['Anik', 'Lies','Fendi'],
              'Anik': ['Luthfi', 'Andin'],
              'Didik': ['Luthfi', 'Andin'],
              'Andin': ['naura'],
              'Luthfi': ['farhan', 'arfan'],
              'Lies': ['Hanan'],
              'Fendi': ['Lia', 'Vano'],
              'ita': ['Lia', 'Vano'] }

def ancestors(genealogy, person):
    list_of_ancestors=[]

    if person in genealogy:
       list_of_ancestors=genealogy[person]
       for e in genealogy[person]:  
            for i in ancestors(genealogy,e):
                if i not in list_of_ancestors:
                    list_of_ancestors+=ancestors(genealogy,e)
    else:
        list_of_ancestors+=[]

    return list_of_ancestors


print(ancestors(ada_family, 'Rofi'))
