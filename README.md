# file-share-LAN
A simple server/client app for sharing files over HTTP for computers in same router!

# Instalation guide
Having installed python, pip3 execute: 

```
pip3 install reqs.txt 
```

# Config server

> In config.cnf set: 
> IP the IP of the machine in the lan
> PORT the desired port to run
> SHARED_LIBS all the libraries to share (currently it is required for the shared libs to be children in the file-share-LAN dir)


# Boot the Server 

Execute: 
```
python3 share.py
```

This can be executed in the background using ``` python3 share.py & ```

# Request a file:

From any machine and/or tool (curl/ Postman) create a GET request http://<ip>:<port>/getfile/<filename> to receive the file named <filename>
