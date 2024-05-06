import modules.corefileCIT as CIT
import funciones.globales as gf
import funciones.citas as uic
import funciones.Pacientes as uiPC
import main

def MenuCitas(op : int):
    title = """
    ********************************
    * ALMINISTRADOR DE AGENDAR CITAS *
    ********************************
    """
    MenuCitasop = "1. agregar cita medica \n2. paciente nuevo \n3 salir"
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(MenuCitasop)
        try:
            op = int(input(":) "))
        except ValueError:
            print("opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            MenuCitas(0)
        else:
            match (op):
                case 1:
                    uic.NewCitas()
                case 2:
                    uiPC.Newpacientes()
                case 3:
                    main.MainMenu(0)
                case _:
                    print("la opcion ingresada no esta disponible en las opciones ")
                    gf.pausar_pantalla()