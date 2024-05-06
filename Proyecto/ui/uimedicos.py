import modules.corefile as cf
import funciones.globales as gf
import funciones.medicos as fm
import main

def MenuMedicos(op : int):
    title = """
    **************************
    * ALMINISTRADOR DE MEDICOS *
    **************************
    """
    MenuMedicosop = "1. agregar\n2. editar\n3. eliminar\n4.salir"
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(MenuMedicosop)
        try:
            op = int(input(":) "))
        except ValueError:
            print("opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            MenuMedicos(0)
        else:
            match (op):
                case 1:
                    fm.Newmedicos()
                case 2:
                    pass#st.ModifyData()
                case 3:
                    main.MainMenu(0)
                case _:
                    print("la opcion ingresada no esta disponible en las opciones ")
                    gf.pausar_pantalla()
                    

