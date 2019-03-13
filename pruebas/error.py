# Ing. Harold Ramírez Herrera
import sys, os, webbrowser, platform, subprocess

import webbrowser

def limpiar():
    if  os.name == 'nt':
            os.system('cls')
    else:
        os.system('clear')
def menu():
        limpiar()


print """
                                                                  \033[1;31m        PRUEBA DE HERRAMIENTAS
                                                                  \033[1;34m           ERROR404 
                                                                  \033[1;35m  Recopilación De Información
"""


print '''
                                        \033[1;32m 1. Usersherlock 	                 
                                        \033[1;32m 2. Usersearch	                    
                                        \033[1;32m 3. Namechk    	             
                                        \033[1;32m 4. linkedin    	                
                                        \033[1;32m 5. About.me                              
                                        \033[1;32m 6. Pipl   		         
	                                \033[1;32m 7. GoogleProfile
	                                \033[1;32m 8. Twitter
	                                \033[1;32m 9. Facebook  
	                                \033[1;32m 10.Instagram  
	                                \033[1;32m 11.EPS 
	                                \033[1;32m 12.Libreta militar
	                                \033[1;32m 13. Comparendos 
	                                \033[1;32m 14. Antecedentes 
	                               \033[1;32m  15. RUNT   	
	                                \033[1;32m 16. Sisben  
	                                \033[1;32m 17. Salir  	  
		'''
d = raw_input("\033[1;30m DOXING ERROR404 > ")

if d == "1":
    webbrowser.open('http://usersherlock.com/')
    menu()
elif d == "2":
    webbrowser.open('https://www.usersearch.org/')
    menu()
elif d == "3":
    webbrowser.open('http://namechk.com/')
    menu()
    
elif d == "4":
    webbrowser.open('http://www.linkedin.com/')
    menu()
elif d == "5":
    webbrowser.open('https://about.me/')
    menu()
elif d == "6":
    webbrowser.open('https://pipl.com/')
    menu()
elif d == "7":
    webbrowser.open('https://profiles.google.com/')
    menu()
elif d == "8":
    webbrowser.open('https://twitter.com/')
    menu()
elif d == "9":
    
    webbrowser.open('http://www.facebook.com/')
    menu()
elif d == "10":
    webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
    menu()
elif d == "11":
    webbrowser.open('http://www.fosyga.in/fosyga/')
    menu()
elif d == "12":
    webbrowser.open('https://www.libretamilitar.mil.co/modules/consult/militarysituation')
    menu()
elif d == "13":
    webbrowser.open('https://www.simbogota.com.co/index.php?option=com_content&view=article&id=419&Itemid=376')
    menu()
elif d == "14":
    webbrowser.open('https://antecedentes.policia.gov.co:7005/WebJudicial/formAntecedentes.xhtml')
    menu()
elif d == "15":
    webbrowser.open('https://www.runt.com.co/consultaCiudadana/#/consultaPersona')
    menu()
elif d == "16":
    webbrowser.open('http://www.sisben.gov.co/atencion-al-ciudadano/Paginas/consulta-del-puntaje.aspx')
    menu()
elif d == "17":
    sys.exit()

menu()
