def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""     
    nb_sec = temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]    
    return nb_sec  
  
  
  
mon_temps = (3,23,1,34)
mon_lendemain =(4,23,1,34) print(type(mon_temps)) 
mon_nb_sec=tempsEnSeconde(mon_temps) 
print(mon_nb_sec)
mon_nb_sec=tempsEnSeconde(mon_lendemain) 
print(mon_nb_sec)


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""

minutes = seconde//60
heures = seconde//3600
jours = seconde//(24*3600)
temps = jours , heures , minutes , seconde 
print(temps)


    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
