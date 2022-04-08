
# Servidor FTP

## Índice

### [1 Introducción](#1--Introducción)

### [2 Requerimientos](#2--Requerimientos)

### [3 Preparación](#3--Preparación)
#### &nbsp; &nbsp; [3.1 Instalación](#31--Instalación)
#### &nbsp; &nbsp; [3.2 Configuración](#32--Configuración)
#### &nbsp; &nbsp; [3.3 Comprobación](#33--Comprobación)
#### &nbsp; &nbsp; [3.4 Habilitación del usuario anónimo](#34--Habilitación-del-usuario-anónimo)
#### &nbsp; &nbsp; [3.5 Comprobación del usuario anónimo](#35--Comprobación-del-usuario-anónimo)
#### &nbsp; &nbsp; [3.6 Seguridad](#36--Seguridad)
##### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [3.6.1 Conexión por SSL](#361--Conexión-por-SSL)
##### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [3.6.2 Establecimiento de cuotas de usuario](#362--Establecimiento-de-cuotas-de-usuario)
##### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [3.6.3 Cortafuegos](#363--Cortafuegos)
#### &nbsp; &nbsp; [3.7 Comprobación de la seguridad](#37--Comprobación-de-la-seguridad)

### [4 Webgrafía](#4--Webgrafía)

### [5 Conclusión](#5--Conclusión)

---

## 1  Introducción

El protocolo de red FTP (File Transfer Protocol) sirve para la transferencia de archivos en una red TCP basado en una arquitectura cliente-servidor independientemente del sistema operativo usado en cada equipo y utilizando normalmente los puertos de red 20 y 21.  

En una empresa la aplicación más común de un servidor FTP es el alojamiento donde los clientes suben sus archivos correspondientes, o para almacenar copias de seguridad o archivos de configuración de servidores.

## 2  Requerimientos

Todas las máquinas virtuales tienen el sistema operativo Debian 9 stretch.

- Hipervisor VMware Workstation.

- Servidor ssh en las máquinas virtuales.

- Cliente ssh en la máquina anfitriona.

## 3  Preparación

En una máquina virtual accedemos mediante ssh desde la máquina anfitriona.

### 3.1  Instalación

Escribimos el comando, `# apt install vsftpd`, para instalar el servidor vsftp, y escribimos el comando, `# netstat -putan | egrep vsftpd`, para comprobar que esta escuchando peticiones el servicio vsftpd.

<div align="center">
	<img src="imagenes/Instalacion/Captura.PNG" alt="Instalación del servidor vsftpd.">
</div>

<div align="center">
	<img src="imagenes/Instalacion/Captura1.PNG" alt="Habilitación del servidor vsftpd." width="600px">
</div>

### 3.2  Configuración

Escribimos el comando, `# nano /etc/vsftpd.conf`, y escribimos el contenido.

	userlist_enable=YES # Habilitación de la lista de usuarios del servidor vsftpd  
	userlist_file=/etc/vsftpd.userlist  
	userlist_deny=NO  
	  
	write_enable=YES # Habilitación de permisos de escritura a los usuarios  
	local_umask=022 # Establecer permisos a los archivos creados  
	  
	chroot_local_user=YES # Enjaulamiento de los usuarios  
	user_sub_token=$USER  
	local_root=/home/$USER/ftp  
	  
	# Establecer puertos pasivos del servidor vsftpd  
	pasv_min_port=40000  
	pasv_max_port=40100  

<div align="center">
	<img src="imagenes/Configuracion/Captura.PNG" alt="Configuración del archivo del sevidor vsftpd." width="600px">
</div>

Escribimos el comando, `# nano /etc/vsftpd.userlist`, y escribimos el nombre de los usuarios especificados.

<div align="center">
	<img src="imagenes/Configuracion/Captura1.PNG" alt="Habilitación de los usuarios del servidor vsftpd." width="600px">
</div>

Escribimos el comando, `# chown nobody:nogroup /home/raulgp/ftp`, escribimos el comando, `# chmod 555 /home/raulgp/ftp`, para establecer los permisos del directorio del usuario vsftpd especificado.

<div align="center">
	<img src="imagenes/Configuracion/Captura3.PNG" alt="Establecimiento de los permisos del directorio del usuario vsftpd." width="600px">
</div>

<div align="center">
	<img src="imagenes/Configuracion/Captura4.PNG" alt="Verificación de los permisos del directorio del usuario vsftpd." width="600px">
</div>

Escribimos el comando, `# chown raulgp:raulgp /home/raulgp/ftp/"nombre de archivo"`, para cambiar el propietario y el grupo donde el usuario vsftpd subirá sus archivos en la carpeta especificada.

<div align="center">
	<img src="imagenes/Configuracion/Captura5.PNG" alt="Establecimiento del propietario y del grupo del directorio de subida de archivos." width="600px">
</div>

<div align="center">
	<img src="imagenes/Configuracion/Captura6.PNG" alt="Verificación del propietario y del grupo del directorio de subida de archivos." width="600px">
</div>

Escribimos el comando, `# service vsftpd restart`, para reiniciar el servidor vsftpd.

<div align="center">
	<img src="imagenes/Configuracion/Captura7.PNG" alt="Reinicio del servidor vsftpd.">
</div>

### 3.3  Comprobación

Nos vamos a otra máquina virtual, escribimos el comando, `# ftp 192.168.20.15`, escribimos el nombre de usuario, y escribimos la contraseña.

<div align="center">
	<img src="imagenes/Comprobacion/Captura.PNG" alt="Verificación del servicio vsftpd mediante cliente por línea de comandos.">
</div>

Nos vamos a la máquina anfitriona, ejecutamos el cliente FileZilla, escribimos la dirección IP del servidor, escribimos el nombre de usuario, escribimos la contraseña, y le damos a conexión rápida.

<div align="center">
	<img src="imagenes/Comprobacion/Captura1.PNG" alt="Verificación del servicio vsftpd mediante cliente gráfico" width="900px">
</div>

Nos vamos al servidor vsftpd, y escribimos el comando, `# tcpdump -i "interfaz de red" tcp`, comprobamos que los puertos pasivos utilizados son entre el 40000 al 40100.

<div align="center">
	<img src="imagenes/Comprobacion/Captura3.PNG" alt="Verificación de los puertos pasivos utilizados en el servidor vsftpd.">
</div>

Escribimos el comando, `# vsftpdwho`, para mostrar los usuarios conectados en el servidor vsftpd.

<div align="center">
	<img src="imagenes/Comprobacion/Captura2.PNG" alt="Verificación de la conexión establecida de usuarios en el servidor vsftpd." width="600px">
</div>

### 3.4  Habilitación del usuario anónimo

Escribimos el comando, `# nano /etc/vsftpd.conf`, y escribimos el contenido.

	ftpd_banner=Bienvenido al servidor vsftpd de raulgp. # Habilitación del mensaje de bienvenida
	idle_session_timeout=120 # Establecer tiempo de cierre de sesión por inactividad
	
	anon_umask=266 # Establecer permisos a los archivos del usuario anónimo
	anonymous_enable=YES # Habilitación del usuario anónimo
	dirmessage_enable=YES # Habilitación del mensaje de bienvenida del usuario anónimo
	anon_world_readable_only=YES # Habilitación de permisos de solo lectura al usuario anónimo
	anon_max_rate=204800 # Establecer tasa de transferencia
	accept_timeout=600 # Establecer tiempo de cierre de sesión por inactividad al usuario anónimo
	allow_anon_ssl=NO # Deshabilitación de la conexión establecida del usuario anónimo por SSL

<div align="center">
	<img src="imagenes/Habilitacion_del_usuario_anonimo/Captura.PNG" alt="Configuración del archivo del servidor vsftpd." width="600px">
</div>

Escribimos el comando, `# nano /etc/vsftpd.userlist`, y escribimos el nombre del usuario anónimo especificado.

<div align="center">
	<img src="imagenes/Habilitacion_del_usuario_anonimo/Captura3.PNG" alt="Habilitación del usuario anónimo del servidor vsftpd." width="600px">
</div>

Escribimos el comando, `# nano /srv/ftp/.message`, y escribimos el mensaje de bienvenida del usuario anónimo.

<div align="center">
	<img src="imagenes/Habilitacion_del_usuario_anonimo/Captura1.PNG" alt="Habilitación del mensaje de bienvenida del usuario anónimo del servidor vsftpd." width="600px">
</div>

Escribimos el comando, `# service vsftpd restart`, para reiniciar el servidor vsftpd.

<div align="center">
	<img src="imagenes/Habilitacion_del_usuario_anonimo/Captura2.PNG" alt="Reinicio del servidor vsftpd.">
</div>

### 3.5  Comprobación del usuario anónimo

Nos vamos a otra máquina virtual, escribimos el comando, `# ftp 192.168.20.15`, escribimos el nombre de usuario, y escribimos la contraseña.

<div align="center">
	<img src="imagenes/Comprobacion_del_usuario_anonimo/Captura.PNG" alt="Verificación de la habilitación del usuario anónimo del servidor vsftpd mediante cliente por línea de comandos." width="600px">
</div>

Escribimos el comando, `# vsftpdwho`, para mostrar los usuarios conectados en el servidor vsftpd.

<div align="center">
	<img src="imagenes/Comprobacion_del_usuario_anonimo/Captura2.PNG" alt="Verificación de la conexión establecida del usuario anónimo en el servidor vsftpd." width="600px">
</div>

Nos vamos a la máquina anfitriona, ejecutamos el cliente FileZilla, escribimos la dirección IP del servidor, escribimos el nombre de usuario, escribimos la contraseña, y le damos a conexión rápida.

<div align="center">
	<img src="imagenes/Comprobacion_del_usuario_anonimo/Captura1.PNG" alt="Verificación de la habilitación del usuario anónimo del servidor vsftpd mediante cliente gráfico." width="900px">
</div>

### 3.6  Seguridad

Escribimos el comando, `# nano /etc/vsftpd.conf`, y escribimos el contenido.

	listen=YES
	listen_ipv6=NO # Deshabilitación de escucha de peticiones en IPv6
	
	xferlog_file=/var/log/vsftpd.log # Habilitación del log
	
	listen_port=21 # Establecer puerto de escucha de peticiones
	listen_address=192.168.20.15 # Establecer la dirección IP de la interfaz de red de escucha de peticiones
	max_clients=5 # Establecer número máximo de usuarios
	max_per_ip=5 # Establecer número máximo de usuarios en la misma interfaz de red

<div align="center">
	<img src="imagenes/Seguridad/Captura.PNG" alt="Configuración del archivo del servidor vsftpd." width="600px">
</div>

<div align="center">
	<img src="imagenes/Seguridad/Captura1.PNG" alt="Configuración del archivo del servidor vsftpd." width="600px">
</div>

#### 3.6.1  Conexión por SSL

Escribimos el comando, `# openssl genrsa 4096 > /home/raulgp/certificadoseg.key`, para generar la clave del certificado SSL especificado.

<div align="center">
	<img src="imagenes/Seguridad/Captura3.PNG" alt="Generación de la clave del certificado SSL." width="600px">
</div>

Escribimos el comando, `# chown root:ssl-cert /home/raulgp/certificadoseg.key`, y escribimos el comando, `# chmod 640 /home/raulgp/certificadoseg.key`, para establecer los permisos de la clave del certificado SSL especificado.

<div align="center">
	<img src="imagenes/Seguridad/Captura4.PNG" alt="Establecimiento de los permisos de la clave del certificado SSL." width="600px">
</div>

<div align="center">
	<img src="imagenes/Seguridad/Captura5.PNG" alt="Verificación de los permisos de la clave del certificado SSL." width="600px">
</div>

Escribimos el comando, `# openssl req -new -x509 -nodes -sha1 -days 365 -key /home/raulgp/certificadoseg.key > /home/raulgp/certificadoseg.pem`, para generar el certificado SSL especificado.

<div align="center">
	<img src="imagenes/Seguridad/Captura6.PNG" alt="Generación del certificado SSL." width="800px" height="400px">
</div>

Escribimos el comando, `# nano /etc/vsftpd.conf`, y escribimos el contenido.

	allow_anon_ssl=YES # Habilitación de la conexión establecida del usuario anónimo por SSL
	
	rsa_cert_file=/home/raulgp/certificadoseg.pem
	rsa_private_key_file=/home/raulgp/certificadoseg.key
	ssl_enable=YES # Habilitación de la conexión establecida por SSL

<div align="center">
	<img src="imagenes/Seguridad/Captura7.PNG" alt="Configuración del archivo del servidor vsftpd." width="600px">
</div>

Escribimos el comando, `# service vsftpd restart`, para reiniciar el servidor vsftpd.

<div align="center">
	<img src="imagenes/Seguridad/Captura8.PNG" alt="Reinicio del servidor vsftpd.">
</div>

#### 3.6.2  Establecimiento de cuotas de usuario

Escribimos el comando, `# apt install quota quotatool`, escribimos el comando, `# nano /etc/fstab`, y escribimos las opciones, `usrquota,grpquota`, para establecer las opciones de montaje de los dispositivos especificados.

<div align="center">
	<img src="imagenes/Seguridad/Captura10.PNG" alt="Instalación de las cuotas de usuario.">
</div>

<div align="center">
	<img src="imagenes/Seguridad/Captura11.PNG" alt="Configuración del archivo de montaje de dispositivos.">
</div>

Escribimos el comando, `# mount -o remount,rw /`, para montar los dispositivos especificados.

<div align="center">
	<img src="imagenes/Seguridad/Captura12.PNG" alt="Montaje con opciones del dispositivo principal en el servidor vsftpd.">
</div>

Escribimos el comando, `# quotacheck -cgum /`, escribimos el comando, `# edquota -u "nombre de usuario"`, y escribimos el contenido.

<div align="center">
	<img src="imagenes/Seguridad/Captura13.PNG" alt="Habilitación de las cuotas de usuario en el dispositivo principal en el servidor vsftpd.">
</div>

<div align="center">
	<img src="imagenes/Seguridad/Captura14.PNG" alt="Establecimiento de las cuotas de usuario." width="700px">
</div>

Escribimos el comando, `# repquota / -s`, para comprobar las cuotas de usuario en el dispositivo especificado.

<div align="center">
	<img src="imagenes/Seguridad/Captura15.PNG" alt="Verificación de las cuotas de usuario." width="600px">
</div>

Escribimos el comando, `# edquota -g "nombre de grupo"`, y escribimos el contenido.

<div align="center">
	<img src="imagenes/Seguridad/Captura16.PNG" alt="Establecimiento de las cuotas de grupo." width="700px">
</div>

Escribimos el comando, `# repquota / -sg`, para comprobar las cuotas de grupo en el dispositivo especificado.

<div align="center">
	<img src="imagenes/Seguridad/Captura17.PNG" alt="Verificación de las cuotas de grupo." width="600px">
</div>

#### 3.6.3  Cortafuegos

Escribimos el comando, `# nano regvsftpdiptables.sh`, y escribimos el contenido.

	# Limpieza de todas las reglas y denegar o aceptar las conexiones  
	iptables -F  
	iptables -X  
	iptables -Z  
	iptables -t nat -F  
	iptables -P INPUT DROP  
	iptables -P FORWARD DROP  
	iptables -P OUTPUT ACCEPT  
	  
	# Aceptar los protocolos y los puertos de entrada en las interfaces de red  
	iptables -A INPUT -i lo -p all -j ACCEPT  
	iptables -A INPUT -i ens33 -p icmp -j ACCEPT  
	iptables -A INPUT -p tcp --dport 20 -j ACCEPT  
	iptables -A INPUT -p tcp --dport 21 -j ACCEPT  
	iptables -A INPUT -p tcp --dport 22 -j ACCEPT  
	iptables -A INPUT -p tcp --dport 40000:40100 -j ACCEPT

<div align="center">
	<img src="imagenes/Seguridad/Captura9.PNG" alt="Configuración de las reglas de iptables." width="600px">
</div>

### 3.7  Comprobación de la seguridad

Escribimos el comando, `# netstat -putan | egrep vsftpd`, para comprobar que esta escuchando peticiones en el puerto y en la interfaz de red especificadas el servicio vsftpd.

<div align="center">
	<img src="imagenes/Comprobacion_de_la_seguridad/Captura.PNG" alt="Puerto e interfaz de red de escucha de peticiones del servidor vsftpd." width="700px">
</div>

Nos vamos a la máquina anfitriona, ejecutamos el cliente FileZilla, escribimos la dirección IP del servidor, escribimos el nombre de usuario, escribimos la contraseña, le damos a conexión rápida, comprobamos que excedemos el número máximo de usuarios establecido.

<div align="center">
	<img src="imagenes/Comprobacion_de_la_seguridad/Captura1.PNG" alt="Verificación del exceso de número máximo de usuarios." width="700px">
</div>

Nos vamos al servidor vsftpd, escribimos el comando, `# tail /var/log/vsftpd.log`, para mostrar el log del servidor vsftpd.

<div align="center">
	<img src="imagenes/Comprobacion_de_la_seguridad/Captura2.PNG" alt="Log del servidor vsftpd." width="600px">
</div>

Nos vamos a la máquina anfitriona, ejecutamos el Wireshark, seleccionamos la interfaz de red especificada, le damos a capturar, le damos a empezar, comprobamos que la conexión establecida esta encriptada.

<div align="center">
	<img src="imagenes/Comprobacion_de_la_seguridad/Captura3.PNG" alt="Verificación de la conexión establecida encriptada.">
</div>

Ejecutamos el cliente FileZilla, escribimos la dirección IP del servidor, escribimos el nombre de usuario, escribimos la contraseña, le damos a conexión rápida, subimos un archivo, comprobamos que excedemos la cuota de usuario especificada.

<div align="center">
	<img src="imagenes/Comprobacion_de_la_seguridad/Captura4.PNG" alt="Verificación del exceso de la cuota de usuario." width="900px">
</div>

Nos vamos al servidor vsftpd, escribimos el comando, `# iptables -L`, para mostrar las reglas de iptables establecidas.

<div align="center">
	<img src="imagenes/Comprobacion_de_la_seguridad/Captura5.PNG" alt="Verificación del establecimiento de las reglas de iptables." width="600px">
</div>

## 4  Webgrafía

<https://linux.die.net/man/5/vsftpd.conf>  
<https://krypted.com/unix/customizing-vsftpd-banners/>  
<https://www.zeppelinux.es/instalacion-y-configuracion-del-servidor-ftp-vsftpd-en-linux-debian/>  
<https://linuxize.com/post/how-to-setup-ftp-server-with-vsftpd-on-debian-9/>

## 5  Conclusión

Un servidor ftp es una manera sencilla de que los usuarios permitidos puedan subir o descargar archivos.
