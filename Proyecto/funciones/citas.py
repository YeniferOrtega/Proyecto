import json
import os
import funciones.globales as gf
import modules.corefile as cf
import modules.corefile as  cfhs
import ui.uicitas as uic

def NewCitas():
    title ="""
    *************************
    * AGENDA DE CITAS MEDICAS *
    *************************
    """
    gf.borrar_pantalla()
    print(title)

    identificacion = input('ingrese numero de identidad del paciente : ')
    paciente_existente = searchData(identificacion)
    if paciente_existente:
        print("datos de paciente: ")
        print(json.dumps(paciente_existente, indent=4))
    else:
        print('paciente no se encuentra por favor porpocione la informacion : ')
        codpaciente = input('ingrese codigo de paciente : ')
        nombrepaciente = input('ingresar nimbre del paciente : ')
        telefono = input('ingresar numero de telefono : ')

        pacientes ={
            "identificacion" : identificacion,
            "codpaciente" : codpaciente,
            "nombrepaciente" : nombrepaciente
        }

        # agregar nuevo paciente a base de datos
        cf.AddData('data', identificacion,pacientes, codpaciente, telefono)
        gf.mi_clinica_medica.get('data').update({identificacion : pacientes})

        jornada = input('quiere la cita por la mañana (m) o en la tarde (t) ')
        if jornada.upper() == 'm' :
            horario = input('A que hora por la mañana (07:00 - 11:00) : ')
        elif jornada.upper() == 't' :
            horario = input('A que hora por la tarde (13:00 - 20:00) : ')
        else:
            print('opcion de la jornada no es valida ')
            return
        medicos = input('que especialista desea para la cita ')

        # guardar en Json de citasHisto
        cita = {
            "identificacion" : identificacion,
            "horario" : horario,
            "medicos" : medicos
        }
        cfhs.AddData('citasHisto', identificacion, cita, horario, medicos)

        print('cita agendada con exito')
        uic.MenuCitas(0)

def searchData(identificacion):
    # buscar base de pacientes
    return gf.mi_clinica_medica.get('data').get(identificacion)

def modifyData():
    print (gf.mi_clinica_medica())
    identificacion = input('ingresar numero de identidad que desea modificar : ')
    datapacientes = searchData(identificacion) 

    if not datapacientes.keys():
        print('paciente no se encuentra : ')
        return
    
    print('datos de pacientes : ')
    print(json.dumps(datapacientes, indent=4))

    for key in datapacientes.keys():
        if (key != 'identificacion' and key != 'notas'):
            if bool(input(f'desea modificar {key}? (s para si, enter para no): ')):
               nuevo_valor = input(f'ingrese el nuevo valor para {key}: ')
               datapacientes[key] = nuevo_valor

    gf.mi_clinica_medica.get('data').update({identificacion: datapacientes})
    cf.UpdateFile(gf.mi_clinica_medica)
    cfhs.UpdateFile(gf.mi_clinica_medica)
    print('datos del paciente actualizado en exito')
    uic.MenuCitas(0)


