import json
import os
import funciones.globales as gf
import modules.corefile as cf
import ui.uimedicos as uiMc

def Newmedicos():
       title ="""
        ********************
        * registro medicos  *
        ********************
    """
       gf.borrar_pantalla()
       print(title)
       identificacion = input('ingrese el numero de identificacion : ')
       codmedico = input('ingrese codigo del medico : ')
       nombremedico = input('ingrese nombre del medico : ')
       especialista = input('ingrese su especialisacion')
       medico ={
              'identificacion' : identificacion,
              'codmedico' : codmedico,
              'nombremedico' : nombremedico,
              'medico' :especialista
       }
       cf.AddData('data',identificacion,medico)
       gf.mi_clinica_medica.get('data').update({identificacion:medico})
       if(bool(input('desea registrar otro medico s(si) o enter (no)'))):
              Newmedicos()
       else:
              uiMc.MenuMedicos(0)

def SearchData():
    criterio = input('Ingrese el Nro Identificacion del medico: ')
    data= gf.mi_clinica_medica.get('data').get(criterio)
    return data
    

def ModifyData():
    dataespecialista = SearchData()
    identificacion,codmedico,nombremedico, = dataespecialista.values()
    for key in dataespecialista.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                dataespecialista[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.mi_clinica_medica.get('data').update({identificacion:dataespecialista})
    cf.UpdateFile( gf.mi_clinica_medica.get)
    uiMc.MenuMedicos(0)
                     