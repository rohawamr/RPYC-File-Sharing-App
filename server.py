import rpyc
import os
from rpyc.utils.server import ThreadedServer

class Service(rpyc.Service):
  def on_connect(self):
    print "Someone joined!"
    pass

  def on_disconnect(self):
    print "Someone left!"
    pass
  
  def exposed_fileWriter(self, contents, filename, username):
    f = os.listdir("secure")
    # Checking if files with the same name exist and giving it a new name
    if any(filename in f for filename in f):   
      k = open("secure/new"+filename,"wb+")
      if k.mode == "wb+":
        k.write(contents)
        print "\n The file '"+filename+"' from "+username+" has been transmitted to the SERVER successfully! \n"
      k.close()
    else:
      k = open("secure/"+filename,"wb+")
      if k.mode == "wb+":
        k.write(contents)
        print "\n The file '"+filename+"' from "+username+" has been transmitted to the SERVER successfully! \n"
      k.close()
    
  def exposed_download(self, fname):
      for fname in os.listdir("secure"): 
          try:
            f = open("secure/"+fname,"rb")
            if f.mode == "rb":
              contents = str(f.read())
            f.close()
            return str(contents)
          except IOError:
            return "NF"

  def exposed_disp_list(self):
      return os.listdir("secure")
       
  

    

if __name__ == "__main__":
  # Create a Secure folder which can only be accessed by the Server
  if (os.path.isdir("secure/")) == False:
    os.mkdir("secure",0700)
    print "\n Secure Folder Created! \n"
  t = ThreadedServer(Service, port = 18861)
  t.start()
