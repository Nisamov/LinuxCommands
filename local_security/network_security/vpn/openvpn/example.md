<!-- Pendiente de corregir y establecer formato -->
Una VPN es una conexión remota (crea una camino virtual a través de internet para conectarse sin una conexión).

Instalación de requisitos:
`sudo apt update && sudo apt install -y vsftpd openssh-server ftp openssl git openvpn`

Clonación de Repositorio:
`git clone https://github.com/OpenVPN/easy-rsa-old`
`cp easy-rsa-old`

Establecimiento de Red Estática:
[Revisar apuntes de redes estáticas.](/networking/netplan_net/static-network.conf)
`nano /etc/netplan/00-network-manager-all.yml`	(Los espacios son de 2uds)
```yaml
└────network:
	├──────version: 2
	├──────renderer: networkd (por defecto está NetworkManager)
	├──────ethernets:
	├────────enp0s3:
	├──────────dhcp4: no
	├──────────addresses: [192.168.10.10/24]
	├──────────gateway4: 192.168.10.1
	├──────────nameservers:
	└────────────addresses: [8.8.8.8]
```
Aplicación de cambios en red: `netplan apply`

Clonación de rsa:
`cp -r ./easy-rsa-old/easy-rsa/2.0/ easy-rsa`

Información:
- `build-ca` Crear certificado autorizado
- `build-dh` Diff hellman (encripta todo el trayecto de comunicación)
- `build-key-server` Llaves de certificados de servidor
- `build-key` Llaves de certificado de cliente
- `vars` Archivo donde se indica ubicación, cliente (por defecto Estados Unidos - San Francisco)

Archivo vars:
`nano vars`
```conf
export KEY_COUNTRY=”Country”
export KEY_PROVINCE=”Province”
export KEY_CITY=”City”
export KEY_ORG=”Key”
export KEY_EMAIL=”email@dom.x”
export KEY EMAIL=”email@host.domain”
export KEY_CN=key
export KEY_NAME=key_name
export KEY_OU=Key_Informativa
export PKCS11_MODULE_PATH=DNI Electrónico
export PKCS11_PIN=1234
```

Crear VPN:
```sh
mv openssl.1.0.0.cnf openssl.cnf
. ./vars					>>Propiedades de certificado
./clean-all					>>Borrar certificados creados
./build-ca					>>Crear certificado “ca.crt” dentro de /keys
./build-key-server servidor	>>
./build-dh					>>Crear el dh dentro de /keys
```

Archivo Configuración VPN:
```sh
cd /usr/share/doc/openvpn/examples/sample-config-files
cp server.conf.gz /home/user/easy–rsa/keys
cd /home/user/easy-rsa/keys
```
Comprimir y transformarlo en un archivo legible
```sh
gunzip  server.conf.gz
```
```sh
cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf /home/user/easy-rsa/keys/
```
Descomentar “write_enable=YES”
```sh
nano /etc/vsftpd.conf
```
Reiniciar servicio
```sh
service vsftpd restart
```
Conexión por FTP
```sh
ftp usuario@ip
calve de acceso
put ca.crt
put client.conf
put cliente.key
put cliente.crt
put cliente.csr
```

Información server.conf (servidor) - `nano /home/user/easy-rsa/keys/server.conf`
Establecer dirección de los archivos en máquina servidor
```sh
ca /home/user/easy-rsa/keys/ca.crt
cert /home/user/easy-rsa/keys/servidor.crt
key /home/user/easy-rsa/keys/servidor.key
ifconfig-pool-persist /home/user/easy-rsa/keys/ipp.txt
```
Archivo donde se almacenan las IPs que se le dan a los clientes
```sh
archivo ipp.txt
```
Comentar esta linea
```sh
tls-auth ta.key 0
```
Registro de personas que se loguean
```sh
status /home/user/easy-rsa/keys/openvpn-status.log
```
Iniciar VPN en el servidor
```sh
openvpn server.conf
Información client.conf (cliente)
```
Establecer dirección de los archivos en máquina cliente
```sh
ca /home/user/ca.crt
cert /home/user/cliente.crt
key /home/user/cliente.key
```
Necesario comentar esta línea y contar con la siguiene
```sh
#tls-auth ta.key 0
openvpn user.conf
```