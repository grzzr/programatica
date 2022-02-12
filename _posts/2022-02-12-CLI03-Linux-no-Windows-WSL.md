## Instalar WSL2 no Windows
https://docs.microsoft.com/en-us/windows/wsl/install-manual

- Habilitar WSL 

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

- Habilitar virtualização

 dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
 
 - Reiniciar computador
 
 - Atualizar WSL
 https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
 
 - Marcar WSL2 como default
 
 wsl --set-default-version 2
 
 ## Importar distribuição Linux
 https://docs.microsoft.com/en-us/windows/wsl/use-custom-distro
 
 - Baixar .tar com a distribuição
 
 Alpine Linux miniroot filesystem
 https://www.alpinelinux.org/downloads/
 
 https://dl-cdn.alpinelinux.org/alpine/v3.15/releases/x86_64/alpine-minirootfs-3.15.0-x86_64.tar.gz
 
 --import <Distro> <InstallLocation> <FileName>
 
 C:\Users\gustavo>wsl --import alpine-minirootfs C:\Users\gustavo\AppData\Local\linux\alpine-minirootfs C:\Users\gustavo\AppData\Local\linux\alpine-minirootfs-3.15.0-x86_64.tar
 
 - dar boot no linux
 
 wsl -d alpine-minirootfs
 
 - depois de ter adicionado um usuário (grz) logar com
 
 wsl ~ -u grz
 
 ## Basic commands for WSL
 https://docs.microsoft.com/en-us/windows/wsl/basic-commands
 