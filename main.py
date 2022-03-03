import os
import sys
import re
import datetime
import time


text=input("file:")
text=open(text,"r",encoding="utf8").read()
line_count=text.count("\n")
if text.count("\n") == 0:
  line_count=1
def have(object, have):
  try:
    object[have]
  except IndexError:
    return False
  return True


write=[]
variables={"_file":__file__,"_start": datetime.datetime.now()}
for i in range(line_count+1):
  satir=text.splitlines()
  try:
    satir[i]=re.sub(r'#.*$', "", satir[i])
    belirtec=satir[i].split(":")
    belirtec_sayi=len(belirtec)
    write_sayi=len(write)
    isaretci=satir[i].split(";")
    isaretci_sayi=len(isaretci)
  except IndexError:
    sys.exit()
  
  if len(satir[i].split("="))==2:
    variables[satir[i].split("=")[0]]=satir[i].split("=")[1]
  if isaretci_sayi-1 != 0:
    if isaretci[0] == "exit":
      sys.exit()
    elif isaretci[0] == "vars":
      print(variables)
    elif isaretci[0] == "waitkey":
      input("")
    elif isaretci[0] == "dir":
      print(os.listdir())
    elif isaretci[0] == "consolehistory":
      for x in range(len(write)):
        print(write[x])
    
        
    else:
      print(f"MarkerError '{isaretci[0]}' is not found line:{i}")

  elif belirtec_sayi-1 != 0:
    #program ayarları
    if belirtec[0] == "program":
      if belirtec[1] == "dir":
        os.chdir(belirtec[2])
      elif belirtec[1]=="clear":
        if os.name == "nt":
          os.system("cls")
        else:
          os.system("clear")
      elif belirtec[1]=="run":
        os.system(belirtec[2])
      else:
        print(f"InvalidArgumentError: {belirtec[1]} not found line{i}")

    #wait command
    elif belirtec[0] == "wait":
      try:
        time.sleep(int(belirtec[1]))
      except ValueError:
        print(f"TypeError: Invalid type '{type(belirtec[1])}' intiger required line:{i}")

    elif belirtec[0] == "echo": 
      write.append(belirtec[1])
      
      write[write_sayi]=re.sub(r'#.*$', "", write[write_sayi])
      write[write_sayi]=re.sub(r"--t","    ",write[write_sayi])
      print(write[write_sayi])
    
    elif belirtec[0]=="math":
      toplama=belirtec[1].split("+")
      cikarma=belirtec[1].split("-")
      bolme=belirtec[1].split("/")
      carpma=belirtec[1].split("+")
      print(len(cikarma))
      if len(toplama)!=0:
        #toplama
        print(int(toplama[0])+int(toplama[1]))
      elif len(cikarma)!=0:
        #cikarma
        print(int(cikarma[0])-int(cikarma[1]))
      elif len(bolme)!=0:
        #bolme
        print(int(bolme[0])/int(bolme[1]))
      elif len(carpma)!=0:
        #carpma
        print(int(carpma[1])*int(carpma[2]))
    elif belirtec[0]=="varadd":
      if belirtec[1] in variables:
        try:
          if have(belirtec,2):
            variables[belirtec[1]]=int(variables[belirtec[1]])
            variables[belirtec[1]]+=int(belirtec[2])
          else:
            print(f"ArgumentError: an initiger is required to be added to the variable line:{i}")
        except ValueError as e:
          print(e)
      else:
        print(f"VariableError: Variable '{belirtec[1]}' not found line:{i} ")

      

    elif belirtec[0]=="var":
      try:
        varname=belirtec[1]
      except IndexError:
        print(f"VariableError: Varname required! line:{i}")
      try:
        var=belirtec[2]
        if have(belirtec,3):
          if belirtec[3]=="int":
            variables[varname]=int(var)
          elif belirtec[3]=="float":
            variables[varname]=float(var)
          else:
            print(f"InvalidTypeError: Type '{belirtec[3]}' not defined line:{i}")
        else:
          variables[varname]=var
        
      except IndexError:
        print(f"VariableError: Variable Content required! line:{i}")
      


    elif belirtec[0] == "varget":
      if belirtec[1] in variables:
        print(variables[belirtec[1]])
      else:
        print(f"VariableError: Variable '{belirtec[1]}' not found line:{i}")
    else:
      print(f"adverbError: {belirtec[0]} not found line:{i}")
  
#End of Prob Language
