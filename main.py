import os
import sys
import re

text="""
echo:hello world its soo easy --t hello #This is exam
var:sa:--t
varget:sa
"""
write=[]
variables={"name":"example"}
for i in range(text.count("\n")):
  #Deeğişkenler
  satir=text.splitlines()
  belirtec=satir[i].split(":")
  belirtec_sayi=len(belirtec)
  write_sayi=len(write)
  isaretci=satir[i].split(";")
  isaretci_sayi=len(isaretci)

  if isaretci_sayi-1 != 0:
    if isaretci[0] == "exit":
      sys.exit()
    elif isaretci[0] == "vars":
      print(variables)
    else:
      print(f"MarkerError '{isaretci[0]}' is not found line:{i}")
  if belirtec_sayi-1 != 0:
    if belirtec[0] == "echo":
      write.append(belirtec[1])
      write[write_sayi]=re.sub(r'#.*$', "", write[write_sayi])
      write[write_sayi]=re.sub(r"--t","    ",write[write_sayi])
      print(write[write_sayi])
    elif belirtec[0]=="var":
      try:
        varname=belirtec[1]
      except IndexError:
        print(f"VariableError: Varname required! line:{i}")
      try:
        var=belirtec[2]
        variables[varname]=var
      except IndexError:
        print(f"VariableError: Variable Content required! line:{i}")
      

    elif belirtec[0] == "varget":
      if belirtec[1] in variables:
        print(variables[belirtec[1]])
      else:
        print(f"VariableError: Variable '{belirtec[1]}' not found")
    else:
      print(f"adverbError: {belirtec[0]} not found line:{i}")

