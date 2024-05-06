from modules import corefile as cf
import modules.corefilePA as cfPA
import funciones.globales as fg
import ui.uimedicos as uiMc
import ui.uiPacientes as uiPC
import ui.uicitas as uic

def main():
     cf.MY_DATABASE_es = 'data/especialista.json'
     cf.checkFile(fg.mi_clinica_medica)
     op = 0 # Opcional: puedes definir la opcion que decees enviar a la funcion MainMenu(op)
     MainMenu(op)

def MainMenu(op):
      fg.borrar_pantalla()
      title = """
    *********************************
    * gestion del registro de medicos *
    *********************************
    """
      MainMenuOp = "1. especialista de Pe,Gi,De,En,Opt\n2. pacientes\n3. consultar cita\n4. poner cita\n5. salir "
      if (op != 4):
            print(title)
            print(MainMenuOp)
            try:
                  opcion = int(input(':) '))
            except ValueError:
                  print('error en la occion ingresada')
                  fg.pausar_pantalla()
                  MainMenu(0)
            else:
                match (opcion):
                      case 1: 
                            uiMc.MenuMedicos(0)
                      case 2: 
                            uiPC.MenuPacientes(0)
                      case 3:
                            uic.MenuCitas(0)
                         
                      case 4:
                             print('opcion ingresada no pertenece al menu de opciones')
                             fg.borrar_pantalla()
                      case _:
                          print('opcion no valida ingrese un numero de la lista')
                          fg.pausar_pantalla()
                          
                          MainMenu(0)
if __name__ == '__main__':
     cf.MY_DATABASE_es = 'data/especialista.json'
     cfPA.MY_DATABASE_pa = 'data/pacientes.json'
     cf.checkFile(fg.mi_clinica_medica)
     cfPA.checkFile(fg.mi_clinica_medica)

     MainMenu(0)
            