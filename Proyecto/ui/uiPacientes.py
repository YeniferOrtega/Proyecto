import modules.corefile as cf
import funciones.globales as gf
import funciones.Pacientes as uiPC
import main

def MenuPacientes(op : int):
    title = """
    ****************************
    * ALMINISTRADOR DE PACIENTES *
    ****************************
    """
    MenuPacientesop = "1. agregar\n2. editar\n3. eliminar\n4.salir"
    gf.borrar_pantalla()
    if (op != 3):
        print(title)
        print(MenuPacientesop)
        try:
            op = int(input(":) "))
        except ValueError:
            print("opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            MenuPacientes(0)
        else:
            match (op):
                case 1:
                    uiPC.Newpacientes()
                case 2:
                    uiPC.ModifyData()
                case 3:
                    main.MainMenu(0)
                case _:
                    print("la opcion ingresada no esta disponible en las opciones ")
                    gf.pausar_pantalla()
                    