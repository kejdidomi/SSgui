import os 
import re
from re import search
   
full_executable={"":"empty"}
full_images={"":"empty"}
executable=[]
images=[]
PATH="your-path-here"

for dirpath, dirs, files in os.walk(PATH):  
  for filename in files: 
    fname = os.path.join(dirpath,filename) 
    if fname.endswith('.exe'): 
        full_executable[str(filename)]=str(fname)
        executable.append(filename)
    elif fname.endswith('.img') and (not re.search("-Signal.img$",fname) and filename != "Signal.img"):
        full_images[str(filename)]=str(fname)
        images.append(filename)
  
