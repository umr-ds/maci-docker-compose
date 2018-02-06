#!/bin/bash
cd /maci/maci_backend
umask 0000
chmod 777 -R /maci/maci_backend/AppData/JupyterNotebook
dotnet run
