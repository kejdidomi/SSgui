import os 
import re
from re import search
   
full_executable={"":"empty"}
full_images={"":"empty"}
executable=[]
images=[]

for dirpath, dirs, files in os.walk("D:\FILES\Desktop_D\Y3S1\Signals_and_Systems"):  
  for filename in files: 
    fname = os.path.join(dirpath,filename) 
    if fname.endswith('.exe'): 
        full_executable[str(filename)]=str(fname)
        executable.append(filename)
    elif fname.endswith('.img') and (not re.search("-Signal.img$",fname) and filename != "Signal.img"):
        full_images[str(filename)]=str(fname)
        images.append(filename)
  