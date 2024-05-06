import json
import os
import funciones.globales as gf
import modules.corefilePA as cfPA
import ui.uiPacientes as uiPC

def Newpacientes():
    title ="""
    ***********************
    * registro de pacientes *
    ***********************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input('ingrese el numero de identidad : ')
    codPacientes = input('ingrese el codigo del paciente : ')
    nombrePaciente = input('ingrese nombre del paciente : ')
    telefono = input('ingrese numero telefonico : ')
    pacientes ={
        "identificacion" : identificacion,
        "codPacientes" : codPacientes,
        "nombrePacientes" : nombrePaciente,
        "telefono" : telefono
}
        
    cfPA.AddData('data',identificacion,codPacientes,nombrePaciente,telefono,pacientes)
    gf.mi_clinica_medica.get('data').update({identificacion:pacientes})
    if(bool(input('desea registrar otro medico s(si) o enter (no)'))):
     Newpacientes()
    else:
        uiPC.MenuPacientes(0)

def SearchData():
    criterio = input('Ingrese el Nro Identificacion del paciente : ')
    data=gf.mi_clinica_medica.get('data').get(criterio)
    return data
    

def ModifyData():
    dataPacientes = SearchData()
    identificacion, codPacientes,nombrePacientes,telefono,pacientes = dataPacientes.values()
    for key in dataPacientes.keys():
        if (key != 'identificacion' and key != ''):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                dataPacientes[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.mi_clinica_medica.get('data').update({identificacion:dataPacientes})
    cfPA.UpdateFile(gf.mi_clinica_medica)
    uiPC.MenuPacientes(0)
