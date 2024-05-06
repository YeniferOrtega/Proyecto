import json
import os

MY_DATABASE_pa = 'data/Pacientes.json'

def NewFile(*param):
    with open(MY_DATABASE_pa,"w") as wf:
        json.dump(param[0],wf,indent=4)

def UpdateFile(*param):
    with open(MY_DATABASE_pa,'w') as fw:
        json.dump(param[0],fw,indent=4)

def AddData(*param):
    data = list(param)
    with open(MY_DATABASE_pa,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[data[0]].update({data[1]:data[2]})
        else:
            data_file.update({param[0]})
        # data_file[llavePrincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def ReadFile():
    with open(MY_DATABASE_pa,"r") as rf:
        return json.load(rf)
    
def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE_pa)):
        if(len(param)):
            data[0].Update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])