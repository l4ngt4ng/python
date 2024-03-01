# ___________________

# L i n u x  2 0 2 3
# ___________________

  hack4u ---> codigo de verificacion: 1562-2273-5422-2885







____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                  * * *  k i t t y  s x h d k  r o f i  p o l y b a r    * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

~/.config/sxhkd 

ctrl enter    nueva kitty 
ctrl alt r    run rofi 
ctrl shift p  start polybar 
ctrl shift s  stop polybar
ctrl shift b  burpsuite
ctrl shift n  firejail 

aqui lo que pongas con ctrl shift anda bien 

~/.config/kitty 

T A B S 
n e w  t a b 
                          ctrl shift t   new tab
                          ctrl shift 0   zero number permite establecer el nombre de la tab de la kitty 
                          ctrl shift .   tab a la derecha
                          ctrl shift ,   tab a la izquierda
                                    
                          ctrl shift q   delete tab 
w i n d o w s tmux 
                          n e w  w i n d o w  
                          ctrl shift enter 

                          d e l e t e  w i n d o w 
                          ctrl shift w 

                          m o v i n g 
                          ctrl up/down/left/right move between windows
                          ctrl shift 1 2 3 4 ...
                          r e s i z e      ^
                          ctrl shift -> <- | |
                                             v
                           
                          t o g g l e  l a y o u t 
                          ctrl shift z  establece en primer plano la ventana donde te encuentras 
                          r e o r g a n i z e  windows
                          ctrl shift l 
                          p a n e l  f o r w a r d 
                          ctrl shift f 










____________________________________________________________________________________________________________________________________

#                                      * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
____________________________________________________________________________________________________________________________________



https://overthewire.org/wargames/bandit 



e x e c u t i o n   o u t   c o d e 

echo $?  
0 <--- succesfull 

diferente de 0 hay muchos 1 127 ... <--- E R R O R 

---

stderr 2>/dev/null : la salida error a /dev/null
stdout cat /etc/hosts >/dev/null : estas redirigiendo el output la salida a dev null no se veria el resultado de la ejecucion

si ejecutas : cat /archivonoexiste > /dev/null 2>&1    esto lo que dice es redirige la salida error donde tengas la salida estandar el output 

la forma standart es : cat /archivonoexiste &>/dev/null ni output ni error 

---





____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                      * * *  D E S C R I P T O R E S  D E  F I C H E R O   * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________



1 default filedescriptor to stdout
2 default filedescriptor to stderr 

creas un descriptor de fichero ( necesario escritura para crearlo )

exec 4 <>newFileReadWrite lectura y escritura 
exec 4>newFileWrite lo creas escritura 

lo escribes: 
id  >&4                     
id: write error: Bad file descriptor


lo conviertes a read only
exec 4<newFileWrite  lectura

id  >&4                     
id: write error: Bad file descriptor

Cerrarlo
exec 4>&-

Copias entre descriptores 

creamos el 7 y el 8 nuevos porque el 4 lo cerre antes:

crea el 7 en modo RW y lo asocia al fichero dataFile
~ ❯ exec 7<>dataFile
escribe el whoami output dentro 
~ ❯ whoami >&7 
~ ❯ cat dataFile 
abenito

copio el descriptor de fichero 8 From/del 7 
~ ❯ exec 8>&7
escibo sobre el 8 
~ ❯ id -a >&8

O J O se escribe en el 7 tambien porque son copias
~ ❯ cat dataFile
abenito
uid=1000(abenito) gid=1000(abenito) groups=1000(abenito),10(wheel),970(pkg-build),971(docker),984(libvirt)


7                   8    puedes cerrar el 7 con exec 7>&- y ya no podria    7                   8
|                   |    operar sobre el fichero, pero el ocho sigue        |                   |
|                   |    pudiendo                                           x                   |
 ---> dataFile <----                                                              dataFile <----


Por ultimo a la que creas la copia de un descriptor a otro puedes borrar el original 

exec 8>&7- esto genera la flecha del 8 al archivo que paunta 7 y cierra siete 


---
https://deephacking.tech/permisos-sgid-suid-y-sticky-bit-linux/#:~:text=Permiso%20SGID,-El%20permiso%20SGID&text=Si%20se%20establece%20en%20un,perteneciente%2C%20el%20grupo%20del%20directorio.
https://www.ochobitshacenunbyte.com/2019/06/17/permisos-especiales-en-linux-sticky-bit-suid-y-sgid/
https://www.ibiblio.org/pub/linux/docs/LuCaS/Manuales-LuCAS/SEGUNIX/unixsec-2.1-html/node56.html





____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * *  P E R M I S O S  E S P E C I A L E S  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________



S t i c k y  b i t sobre directorio 
___________________________________ 


si tienes un dir con 777 pongamos 

drwxrwxrwx pepe pepe 190 B ...... pruebasDir   <--- lo pueden escribir todos 
  si dentro tienes un archivo tal .rw-r--r-- pepe pepe filedeprueba <--- puede ser borrado escrito por todos 
  aunque tenga r-- en others porque prevalece el privilegio del directorio que lo contiene 


si al directorio le pones chmod +t pruebasDir nadie lo puede escribir/borrar que no sea el propietario del fichero

drwxrwxrwxt <--- la t pepe pepe 190 B ...... pruebasDir


S U I D 
      |
      v
chmod 4775 file  
chmod u+s  file  

-rwsr-xr-x file 
   ^
   |

cuidado con esto sobre binarios:

~ > ls -las /usr/bin/pkexec                                                                                                                                              1m 40s root@fedorian
32 -rwsr-xr-x 1 root root 32704 Mar 30  2023 /usr/bin/pkexec

vulnerabilidad PwnKit 

para encontrar más: find / -type f -perm -4000 2>/dev/null


EXPLICACION OJO :

~ ❯ ls -las /usr/bin/python3.11                                                                                                                                                           11s
16 -rwxr-xr-x 1 root root 15872 Oct  3 02:00 /usr/bin/python3.11
~ ❯ python3.11                 
Python 3.11.6 (main, Oct  3 2023, 00:00:00) [GCC 13.2.1 20230728 (Red Hat 13.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.setuid(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
PermissionError: [Errno 1] Operation not permitted
>>> quit()


pero si tuviera setuid :

~ ❯ ls -las /usr/bin/python3.11                                                                                                                                                           53s
16 -rwsr-xr-x 1 root root 15872 Oct  3 02:00 /usr/bin/python3.11
~ ❯ id
uid=1000(abenito) gid=1000(abenito) groups=1000(abenito),10(wheel),970(pkg-build),971(docker),984(libvirt)
~ ❯ python3.11
Python 3.11.6 (main, Oct  3 2023, 00:00:00) [GCC 13.2.1 20230728 (Red Hat 13.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.setuid(0)
>>> os.system("whoami")
root
0
>>> os.system("bash")
[root@fedorian ~]# id
uid=0(root) gid=1000(abenito) groups=1000(abenito),10(wheel),970(pkg-build),971(docker),984(libvirt)

te ha dado hasta una bash con root flipa!

PORQUE? porque el binario tiene privilegio de ejecucion con usuario root y aunque tu no seas root 
al ejecutar ese binario se ejecuta en contexto de root y tu puedes escalarlo 



otro ejemplo: 

-rwsr-x--- 1 bandit20 bandit19 7868 May 7 2020 ficheroejecutable.sh 

./ficheroejecutable.sh sh  <--- esto regresa una shell con root 
                       bash -p   es lo mismo 

G U I D
      |
      v
chmod 2775 dir  
chmod g+s  dir  

-rwxr-sr-x dir 
      ^
      | 
pasa idem es bajo el contexto del grupo root 

la asignacion seria chmod g+s /usr/bin/python3.9 por ejemplo 

find / -perm -2000 2>/dev/null


---

/etc/passwd 
tiene una copia /etc/passwd-

---

lsattr & chattr 

~ > touch a                                                                                
~ > lsattr a                                                                               
--------------e------- a
~ > echo "first note" >>a                                                                  
~ > chattr +i a                                                                           
~ > echo "second note" >>a                                                                 
zsh: operation not permitted: a
~ > lsattr a                                                                               
----i---------e------- a





____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * *  C A P A B I L I T I E S  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


https://gtfobins.github.io/

/usr/sbin/mtr-packet cap_net_raw=ep
/usr/sbin/suexec cap_setgid,cap_setuid=ep
...
/usr/bin/newgidmap cap_setgid=ep
/usr/libexec/gstreamer-1.0/gst-ptp-helper cap_net_bind_service,cap_net_admin,cap_sys_nice=ep
/var/lib/docker/overlay2/d7e2d977a07319ca7f4e598dde2e4bdfe6c2b917bfcaf76eb2dcc724333b166a/diff/usr/local/bin/kube-apiserver cap_net_bind_service=ep
/var/lib/snapd/snap/core20/1974/usr/bin/ping cap_net_raw=ep

docker ojo puede eecutar root ya ves tiene ep por todas partes 

pongamos como root te das: 
setcap cap_setuid+ep /usr/bin/python3.9 


luego con otro usuario:

~ ❯ /usr/bin/python3.6
Python 3.6.15 (default, May 26 2023, 00:00:00) 
[GCC 13.1.1 20230511 (Red Hat 13.1.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.setuid(0)
>>> os.system("whoami")
root
0


~ ❯ getcap /usr/bin/python3.6                                                                                                                                                             47s
/usr/bin/python3.6 cap_setuid=ep <---- ep em setuid


para eliminar la cap -r

[root@fedorian ~]# setcap cap_setuid+ep /usr/bin/python3.6
[root@fedorian ~]# getcap /usr/bin/python3.6
/usr/bin/python3.6 cap_setuid=ep

[root@fedorian ~]# setcap -r /usr/bin/python3.6 <---
[root@fedorian ~]# getcap /usr/bin/python3.6










____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * * N V I M    * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


alt u  ( ctrl z ) redo 
0 inicio linea
shift 4 ( $ ) ultimo caracter linea
w desplazamient por palabras
3w se desplaza 3 palabras a la vez
ctrl inicio  primera linea
dw elimina esa palabra 
v modo VISUAL para seeccionar  
  seleccionas con las flechas luego y ( lo copias ) 
  esc o  crea nueva linea y luego p del copy de antes 

  haces shift 4 selecciona hasta el final de linea 
  luego j para la linea siguiente 
  luego y para copiar 
  o para new line 
  p paste 

j 0 .  repite la accion anterior

m a c r o s 

q a 
d w ha borrado una palabra y se graba en la macro 
j para que vaya a la siguiente linea 
d w 
q guarda 

para repertir estas acciones 30 veces pongamos :
30 @ a

s u b s 

Esc shift 7 busqueda /y pones lo que quieras buscar

Esc %s/A/B  cambiara a por b  enter 








____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * * C O M A N D O S   * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


F I N D  &  L O C A T E 
_______________________ 


https://www.hostinger.es/tutoriales/como-usar-comando-find-locate-en-linux/

find / -user root -writabl 2>/dev/null

find / -user root -executable -type f  2>/dev/null


find / -name dex\* 2>/dev/null
find / -name \*exdump\* 2>/dev/null
find / -name dexdump\*.sh 2>/dev/null
find / -name dexdump\*.sh -ls 2>/dev/null

TR 
tr '/' ' '  <--- convierte / a espacios 


_____________________
C R O N d  cron crond
_____________________


https://blog.desdelinux.net/cron-crontab-explicados/


generator: https://www.site24x7.com/es/tools/crontab/cron-generator.html



-----------
N E T C A T netcat nc
-----------

nc servidor puerto 
escribes loque sea 
Wrong! Please enter the correct password 

ncat  este tiene una cosa que nc no tiene y es el cifrado ssl 

ncat --ssl servidor puerto 
escribes contra y padentro!

IMPORTANTE
nc -nlvp puerto <--- levanta un puerto en la maquina 

echo "lemandounapass" | nc server port 


---


---------------------------------------------------
L e c t u r a  A r c h i v o s  E s p e c i a l e s
---------------------------------------------------

cat /home/bandit1/-  <--- con ruta absoluta lo abre 
cat ./-
grep -r "\w" 2>/dev/null  esto hace busqueda recursiva de palabras de todos los arcvhivos poreso muestra el contenido 

cat "filename with spaces" 
cat filename\ eith\ spaces
cat f*

---


-----
S S H 
-----

sshpass -p 'lapassword' ssh user@host -p port  bash <--- esto te regresa una bash antes de ejecutar siquiera el bashrc 

F I R S T 
authorized_keys en equipo destino, con tu publica hace que sea clave autorizada: 
cat id_rsa.pub >authorized_keys 

S E C O N D
si tienes una clave privada id_rsa 
ssh-copy-id -i id_rsa user@host   con esto estas autorizando en el destino a una clave privada 
te va a solicitar la contraseña del usuario con el que conectas 

derivado de esto: si COMPARTES la clave PRIVADA con un usuario, se conectara sin que se le solicite password ni nada
ssh -i id_rsa_private user@machine 

y pa dentro!

LAS CLAVES PRIVADAS HAN DE DISPONER 600 permission 


---


rev comando que reversea una cadena 
echo -e "\n  salto de linea 

find . -type f -readable ! -executable  <--- excluye exes -size 1033c <--- c para bytes -user bandit1 -group bandit2

for i in $(seq 1 20); do ;done

cat "filequetienenespacios entre dos columnas" | xargs <--- los reduce a 1 espacio columna A espacio columna B

doc: https://www.ibidemgroup.com/edu/tutorial-sort-linux-unix/
sort archivo | uniq  con opciones pero siempre primero un sort para que ordene el archivo y uniq funcione ok 

doc : https://victorhckinthefreeworld.com/2021/10/21/el-comando-uniq-de-gnu/
uniq -u <--- lista solo lineas unicas ( no borra duplicados como se creia )
uniq -id  lineas duplicadas o iD para verlas

strings archivo lista las cadenas imprimibles unicamente 

base64 -w 0   unica linea 

echo "prueba" | tee savetofile.txt ( muestra prueba y guarda la salida del pipe en el fichero 

ps -eo command  ( regresa los comandos que se estan ejecutando )


TIMEOUT a un comando en bash:
timeout 1 bash -c "ping -c 1 192.168.1.148 &>/dev/null" && echo "[+] host activo en la red" || echo "[+] host no activo en la red"


mktemp -d   crea un dir temporal cuando no puedes leer /tmp por lo que sea 

port scanner: nmap --open -T5 -v -n -p31000-32000 127.0.0.1 


doc: https://eltallerdelbit.com/comando-diff-ejemplos/
diff


stat fichero te regresa mucha info metadata del fichero fechas d eceeaccion manipulacion etc ... 

watch -n 1 ls -l  para ver que esta pasando 


m o r e  more  M A R A V I L L O S O 
_____________

more fichero  

haciedno tu terminal pequeño, menos de lo que tiene que mostrar del fichero puedes "detener" more y te dice 68% por ejemplo 
esto es la proporcion que te ha mostrado

luego v    entras en modo visual 
esc shift : puedes definir  :set shell=/bin/bash enter
esc shift : shell  ---> te otorga la shell 



s p o n g e sponge 
__________________

permite 

cat file-text.txt |  awk '{print $2}' >file-text.txt   esto SIEMPRE borra el archivo origen y destino que es el mismo archivo 

cat file-text.txt |  awk '{print $2}'| sponge file-text.txt


_________
A W K awk 
_________

cat file | awk  "/name: \"machine1\"/,/machine2:/"  <--- muestra las lineas desde el primer patron hasta el segundo patron 

awk 'NF{print $NF}' ultimo argumetno linea 

NR
docker ps | awk '{if (NR!=1) print $1 ": " $(NF)}' <--- ecluye primer registro ( primera linea ) y muestra primera y ultima columna del resto de lineas

docker ps | awk '{if (NR!=2) print $1 ": " $(NF)}' <--- excluye el segundo registro (segunda linea ) y muestra primera y ultima columna del resto de lineas

______
T R tr
______

echo "\"cadenaconcomillas\"" | tr -d '"'  selas pule al igual que si quieres eliminar ',' de un output '


_________
S E D sed
_________

echo "             un monton de espacios delante" | sed 's/^ *//'   <--- los elimina
---


----------
G I T  git
----------

git log   muestra los commits 
git show  bcd433siwf3qej4r1ro371fp8eee <--- commit para verlo desde consola 
git branch -a  muestra branches 
git tag 
  secret 
    git show secret    


_____________
X A R G S 
_________

xargs -I {} printf "value = %s\n" {} <g   <--- leee cada linea de un fichero y la almacena en una variable value

find . -name 'loquesea' | xargs -I_ rm -fr _    <--- borra cada linea que ha sacado find 

find . -name 'loquesea' -prune -exec rm -fr {} \;  lo mismo y prune es porque find sigue siendo recursivo y 
     aun habiendo borrado luego intenta buscar en esa ubicacion



para quitar el NAME 

NAME 
123454321:sdaddfafsd 
123243433:sadffvfdvf 

docker ps | tail -n+2 regresa 
123454321:sdaddfafsd 
123243433:sadffvfdvf 

docker ps  | tail -n+2 | fzf  la salida se convierte en elegible interactivamente 

instance_selected=$(k get pods | tail -n+2 | fzf)  te lo guardas 
docker ps | awk '{if (NR!=1) print $1 ": " $(NF)}' | fzf  --height 40%   <--- esta ultima cosa es para mostrar  arriba la salida de fzf 



---



d i s o w n & n o h u p 


alternativa 

whireshark &>/dev/null & disown   <--- es lo mismo que nohup whireshark & 


---

---
w h i c h 

which id
/usr/bin/id 

alternativa : command -v id
/usr/bin/id 

---


_______

C U R L 
_______

curl -s -X GET https://htbmachines.github.io/bundle.js | bat -l js <--- regresa los datos en formato javascript 






____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * * A r c h  P a c m a n / P a r u * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

MANUAL : https://www.busindre.com/guia_rapida_y_completa_de_pacman_arch

https://www.makeuseof.com/how-to-install-and-remove-packages-arch-linux/


---

AUR packages

necesitas tener instalade base-devel y git que ya están instalados 
pacman -S base-devel git 

por ejemplo para este package: 
git clone https://aur.archlinux.org/packages/js-beautify
cd js-bautify 
puedes ver lo que contiene : cat PKGBUILD
finalmente makepkg -si  NO ROOT 

---


Pacman packages 
pacman -S <package name>

U P G R A D E 
A veces da conflictos te dice que por ejemplo no puede hacer el upgrade: 
pacman -Syu   porque encuentra packetes ya instalados que son conflictivos 
y te dice que estan en por ejemplo /usr/bin/normalizer 
pues con borrarlos basta para que pueda cursar el upgrade










____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * * O P E N  P O R T S  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

netstat -nat 
ss -nltp 


cat /proc/net/tcp 

[root@fedorian tmp]# cat /proc/net/tcp
  sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode                                                     
   0: 00000000:14EB 00000000:0000 0A 00000000:00000000 00:00000000 00000000   193        0 24551 1 00000000b815e3ea 100 0 0 10 5                     
   1: 0100007F:0277 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 29724 1 00000000870565f3 100 0 0 10 0                     
   2: 0100007F:170C 00000000:0000 0A 00000000:00000000 00:00000000 00000000   107        0 2469470 1 00000000efc878be 100 0 0 10 0                   
   3: 00000000:006F 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 2465 1 000000000625234e 100 0 0 10 0                      
   4: 00000000:0386 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 1963592 1 00000000f8923481 100 0 0 10 0                   
   5: 017AA8C0:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 30152 1 000000009f0e1800 100 0 0 10 5                     
   6: 3600007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000   193        0 24560 1 000000001159d6e5 100 0 0 10 5                     
   7: 0164A8C0:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 34141 1 00000000dd060878 100 0 0 10 5                     
   8: 3500007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000   193        0 24558 1 00000000b37904db 100 0 0 10 5                     
   9: 8601A8C0:83EC FB025DB9:01BB 01 00000000:00000000 02:00000747 00000000  1000        0 2707418 2 000000002310df6a 22 4 0 10 -1                   
  10: 8601A8C0:DC3C 5DF36B22:01BB 01 00000000:00000000 02:00002D44 00000000  1000        0 2707891 2 0000000026c81998 20 4 31 10 -1                  
  11: 8601A8C0:D82A 9A8D4F28:01BB 01 00000000:00000000 02:00000CB4 00000000  1000        0 2712700 2 00000000aaaeb792 37 4 29 7 7                    
  12: 8601A8C0:9AF0 6EC8FA8E:01BB 01 00000000:00000000 00:00000000 00000000  1000        0 2710924 1 0000000071fd1972 20 4 30 10 -1                  
               ^
               |
               son puertos esta columna con python le pones 0x delante y lo convierte

[root@fedorian tmp]# python
Python 3.11.6 (main, Oct  3 2023, 00:00:00) [GCC 13.2.1 20230728 (Red Hat 13.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x14EB
5355
>>> 

y con ibase i obase:

[root@fedorian tmp]# for i in `cat /proc/net/tcp | cut -d ':' -f 3| cut -d ' ' -f1 |sort -u |  xargs`;do echo -e "puerto en HEX : ${i} ---> $(echo "obase=10; ibase=16; ${i}"| bc) - open"; done
puerto en HEX : 14EB ---> 5355 - open
puerto en HEX : 0277 ---> 631 - open
puerto en HEX : 170C ---> 5900 - open
puerto en HEX : 006F ---> 111 - open
puerto en HEX : 0386 ---> 902 - open
puerto en HEX : 0035 ---> 53 - open
puerto en HEX : 0035 ---> 53 - open
puerto en HEX : 0035 ---> 53 - open
puerto en HEX : 0035 ---> 53 - open
puerto en HEX : 9306 ---> 37638 - open
puerto en HEX : ECB6 ---> 60598 - open
puerto en HEX : E10E ---> 57614 - open
puerto en HEX : DC3C ---> 56380 - open


O por medio de : 

le mandas una cadena vacia a un puerto y si esta abierto al concatenar con && se ejecuta el echo porque 
el $? = 0 codigo de estado ok 
en caso de  estar cerrado regresara algo <> 0 por lo que el && no ejecutara el echo 

(echo '' > /dev/tcp/127.0.0.1/$port) 2>/dev/null && echo "[+] $port - OPEN"





____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * * H E X  B A S E 64  C E S A R  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

-----------------------
C i f r a d o  C E S A R
------------------------


rot <--- rota x posiciones de la a-z por ejmplo lo que es una G era una T eso es un rot13 en online hay rotatorios online

a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 

<----------- 23 posiciones 
esto es f e d c b a z y x w v u t  por lo que lo que es una g era una t originalmente 

cat file | tr '[G-ZA-Fg-za-f]' '[T-ZA-St-za-s]' y te lo hace 

esto es rot13 

tambien lo puedes hacer así :
a b c d e f g h i j k l m n
                          13 
cat file | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'


------------------------------
H E X A D E C I M A L  f i l e  
------------------------------
ejemplo: cat /etc/hosts 

si le haces un | xxd   ---> 

[root@fedorian power]# cat /etc/hosts | xxd 
00000000: 3132 372e 302e 302e 3120 2020 6c6f 6361  127.0.0.1   loca
00000010: 6c68 6f73 7420 6c6f 6361 6c68 6f73 742e  lhost localhost.
00000020: 6c6f 6361 6c64 6f6d 6169 6e20 6c6f 6361  localdomain loca
00000030: 6c68 6f73 7434 206c 6f63 616c 686f 7374  lhost4 localhost
00000040: 342e 6c6f 6361 6c64 6f6d 6169 6e34 2077  4.localdomain4 w
00000050: 7777 2e6e 6769 6e78 6b38 732e 6c6f 6361  ww.nginxk8s.loca
00000060: 6c0a 3a3a 3120 2020 2020 2020 2020 6c6f  l.::1         lo
00000070: 6361 6c68 6f73 7420 6c6f 6361 6c68 6f73  calhost localhos
00000080: 742e 6c6f 6361 6c64 6f6d 6169 6e20 6c6f  t.localdomain lo
00000090: 6361 6c68 6f73 7436 206c 6f63 616c 686f  calhost6 localho
000000a0: 7374 362e 6c6f 6361 6c64 6f6d 6169 6e36  st6.localdomain6
000000b0: 0a31 3932 2e31 3638 2e31 3232 2e36 3720  .192.168.122.67 
000000c0: 206d 310a 3139 322e 3136 382e 3132 322e   m1.192.168.122.
000000d0: 3230 3720 7731 0a31 3932 2e31 3638 2e31  207 w1.192.168.1
000000e0: 3232 2e33 3820 7732 0a31 3932 2e31 3638  22.38 w2.192.168
000000f0: 2e31 3232 2e31 3037 206d 320a 3139 322e  .122.107 m2.192.
00000100: 3136 382e 3130 302e 3133 3020 616e 7369  168.100.130 ansi
00000110: 626c 6531 200a 3139 322e 3136 382e 3130  ble1 .192.168.10
00000120: 302e 3135 3120 616e 7369 626c 6532 0a    0.151 ansible2.


despues un xxd -ps se queda con la parte central luego xargs una sola linea y el tr para quitar espacios :

cat /etc/hosts | xxd -ps | xargs | tr -d ' ' >/tmp/etcHostHex.file


recuperas:

[root@fedorian power]# cat /tmp/etcHostHex.file | xxd -ps -r
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4 www.nginxk8s.local
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.122.67  m1
192.168.122.207 w1
192.168.122.38 w2
192.168.122.107 m2
192.168.100.130 ansible1 
192.168.100.151 ansible2


tambien puedes hacer -r en xxd sin ps a un archivo completo

l i s t  o f  s i g n a t u r e s  H E X 
https://en.wikipedia.org/wiki/List_of_file_signatures


por ejemplo abres con ghex un archivo HEX 

1F 8B<--- estos son los dos primeros magic numbers 
1F 8B	␟‹	0	gz tar.gz	GZIP compressed file[53]  INDICA QUE SE TRATA DE UN ARCHIVO COMPRIMIDO
---

NUMERO USUARIOS SYSTEMA
_______________________

who -q 
o 
finger



P A R R O T  U P G R A D E 
__________________________ 


parrot-upgrade   ( SOLO HACER D ESTA MANERA EN PARROT NADA DE apt upgrade que te lo fundes )


---


____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * * G R E P   * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

    #contiene la palabra amor 
    grep 'amor' fichero 
    regresa palabras que continen amor por la izq y por la der ---> amiamornoleimporta22223

    #comienza con amor ---> no muestra lo que sigue
    grep -oP '^amor' fichero 
    regresa solo el patron de coincidencia ---> amor  podrias hacer | wc -l y cuentas cuantas veces 
                                                amor 
                                                .
    #comienza en amor ---> muestra lo que sigue 
    grep -oP '^amor.*' fichero  
    regresa  ---> amor de dios
                amor sincero 

    #acaba en amor    
    grep -oP '.*amor$' fichero 
    regresa  ---> (mi)amor
                0000amor 

    #comienza en amor y termina en amor y te dice la linea  
    grep -oP '^amor$' fichero -n  
    regresa  ---> 3347:amor 
                ^         
                | linea

    awk 'NR==3347' fichero ---> regresa amor 
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * * S C R I P T S  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


#!/bin/sh 


# para el ctrl C 
function ctrl_c(){
  echo -e "\n\n[!] Saliendo...\n"
  exit 1
}

#Ctrl+C
trap ctrl_c INT

---


#c o l o u r s
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"


echo -e "\n${yellowColour}[+]${endColour}${grayColour} Esto es un comment${endColour}"

---


#operador $() dentro de un script
echo "[+] Esta es tu dir ip -> $(ip a | grep eth0 | awk ..... b )"  


#c u r s o r 
tput civis 
.
.
.
tput cnorm 

#esto oculta el cursos mientras se ejecuta | <--- no se verá 

---

#f u n t i o n 

function help(){
  echo -e "\n[+] Usage:"
}

function getMachineName (){
  ipAddress="$1"  #<--- esto es un parametro que le llega  la funcion actua igual $1 para el primero $2 para el segundo...
  echo -e "\n[+] La ip es $ipAddress"
}

g e t o p s ( esto es para programar como un comando con sus parametros) 

#declarar variable 
declare -i parameter_counter=0 

while getops "m:uh" arg;do   #<--- acepta ./script.sh -m o -u o -h 
  case $arg in 
    # OPTARG dentro de un while getops recibe el valor del parametro -m maquina1 recibe maquina1 el valor de ese parametro.
    m) machineName="$OPTARG"; let parameter_counter=1;; # sumatorio con let seria let variable +=1 por ejemplo 
    n) let parameter_counter=2;;
    h) help;;
  esac 
done 

if [ $parameter_counter -eq 1];then # eq para valores enteros == para cadenas de texto 
  searchMachine $machineName #es una funcion 
elif [ $parameter_counter -eq 2 ];then 
  updateFiles # es una funcion 
else 
  help #otra function
fi

---

#I F   T H EN 
#comparar cadenas
if [ "$cadena1" == "$cadena2"];then
  echo "iguales"
else
  echo "diferentes"
fi
#comparar numeros
if [ $numero1 -eq $numero2 ];then ... 
                  1 2 3 ... 
== cadenas
-eq -lt ... int

#cadena tiene contenido 
if [ "$cadenaquetienealgo"];then ... # significa if esta cadena tiene contenido haz lo que sea 

#
---

sumas en bash : 
echo 2+5 | bc 
echo "2+5" | bc 
echo $((2+5))| bc 
echo $((2+5)) 

---


---

i n s i d e  s c r i p t s 

$# numero de argumentos pasados al script 
$* todos los argumentos 
$0 nombre script 
$1 primer arg
$2 segndo arg ...

& T H R E A D S  hilo s

(echo '' > /dev/tcp/127.0.0.1/$port) 2>/dev/null && echo "[+] $port - OPEN" & <--- esto dentrod e un bucle 
va a abrir un hilo por cada una 

[[ ]] vs [ ]

las dobles permiten evaluar cosas como :
uso de () para agrupar [[ 7 < ( a + b -c ) && ( d + 1 )]]
son mas novedosas las singles [] no permiten operaciones complejas de evaluacion en if then 

---


for i in &(seq 1 3 ); do 

for i in {1 .. 3}; do 

diferencia entre ${UNAVARIABLE} y "${UNAVARIABLE}

si UNAVARIABLE=uno dos tres   <--- un strng que contiene espacios >

en un for por ejemplo la primera se evalua con tres vueltas del bucle
la segunda con una sola CONSIDERA EL STRING COMO UNA UNIDAD INDEPENDIENTE DE SU CONTENIDO


__________________
A R R A Y s  array 
__________________

declare -a myArray=(1 2 3 4 5)

echo ${myArray[@0]} <--- muestra el array completo 

i t e r a r 
declare -i position=0 
for element in ${myArray[@0]};do 
  echo "posicion ${position} --- elemento  : : : ${element}"
  let position+=1
done

n u m e l e m e n t s 

echo ${#myArray[@]} #@

l a s t  e l e m e n t 

echo ${myArray[-1]} <--------------------------
                                                \
o t r a o p ci o n                               |
                                                 |
total-elements=${#myArray[@]}                   / 
echo ${myArray[$(($total-elements-1))]}  <-----

Si quieres hacer operaciones recuerda: 

$((valor1+valor2))

$((${myArray[0]}+${myArray[1]}))


a ñ a d i r  v a l o r e s  a l  a r r a y 

myArray+=(5) 

e l i m i n a r  e l e m e n t o s 
  
unset myArray[0]   <--- el primero 
unset myArray[-1]  <--- el último 

IMPORTANTE despues se usar unset hay que redeclarar el Array para que se guarde bien y sea capaz de encontrar los elementos por posicion:

myArray=(${myArray[@]})    <--- importante entre () 
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#                                                 * * * S H E L L L S  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


s h e l l s 



~ ❯ cat /etc/shells
/bin/sh
/bin/bash
/usr/bin/sh
/usr/bin/bash
/usr/bin/tmux
/bin/tmux
/usr/bin/zsh
/bin/zsh

echo $SHELL

/bin/zsh 

Sobre la terminal NO dentro de un script ( que indica el nombre del script ) 

echo $0 

zsh te regresa ---> util saber que $0 es la shell porque a veces vamos a necesitar ejecutar $0 
command $0

cat !$  <--- deposita el ultimo output del ultimo comando 
---


T E R M S 

no hace Ctrl l  ( clear )
TERM=xterm

ctrl k   borra toda la linea 


---


t t y ( tele type writer) is a device 
the terminal session running a shell process is associated with a TTY 

ps -fea | grep bash 
501 29874 19345 0 11:00PM ttys007 0:00:01 bash 
501 29832 29874 0 11:00PM ttys007 0:00:00 grep bash

tty command exposes your terminal running 
/dev/ttys007 <--- 


cuando corres algo con nohup y & desasocias que corra asociado a un TTY por eso si haces ps -fea 
en lugar de tty tendra ?? 

501 29874 19345 0 11:00PM ?? 0:00:01 talscript execuion nohup &




---
s t r a c e 

strace -T ---> timinginformation
strace -f ---> trace child process 
strace -p ---> trace parent process 

strace -Tfp < process id >

d e b u g 

run this before run script 
sudo strace -Tfp $$ 2>&1 | grep -E 'execve' & 

-/runscript.sh 

and strace will show you call var systems 

---



s u b  s h e l l s  f
M U Y  U T I L 

(date -u )
regresara:
Fri Jul 5 21:34:12 UTC 2023

pero esto trata de ejecutar la string que devuelve la propia ejecucion de date : 
"Fri Jul 5 21:34:12 UTC 2023"

$(date -u) y regresa logicamente command not found 
bash: Fri: command not found 



---

-----------------------------------------  B A C K L O G ----------------------------------

--- 

EN DESUSO UTILIZO KITTY AHORA


T M U X 
_______

c r e a t e  s e s s i o n
tmux new -s nombreSesion

ctrl b ,        ---> renombra ventana 
ctrl b shift 4  ---> rename sesion 

c r e a t e  w i n d o w 
ctrl b c        ---> crea una ventana nueva 

s e l e c t  w i n d o w 
ctrl b 1 
       2
       3  ... posiciona en ventana

ctrl b m        ---> permite que por medio de mouse selecciones la ventana ( se desactiva igual )


D E T A C H E D 
ctrl b d   

──╼ $tmux list-sessions
0: 3 windows (created Mon Dec  4 10:38:56 2023)
albertosesion: 3 windows (created Mon Dec  4 10:47:17 2023)

tmux attach -t albertosesion  y a dentro


s p l i t  p a n e l 
ctrl b shift 2  ---> para generar paneles HORIZONTALES dentro de cada ventana
ctrl b shift 5  ---> para generar paneles VERTICALES dentro de cada ventana

ctrl b o        ---> la letra O para moverte por los paneles
ctrl b flechaUP/Down posiciona 


m o v i n g  i n s i d e  p a n e l 
ctrl b manten el control pulsado y flecha arriba o abajo 

moving panel content between panels 
ctrl b  sueltas altgr [ 

c o p y 
ctrl shift c  ( lo que ya hayas seleccionado con el raton o teclas )
ctrl shift v

otra manera en el modo copia en oh my tmux: <--- solo funciona en ohmytmux 
ctrl b  sueltas altgr [ 
    luego ctrl espace  para comenzar con la seleccion hasta flecha o tecla fin 
    alt w  copia lo que hayas seleccionado

ctrl b  sueltas y altgr ]  lo pega

k i l l  p a n e l 
ctrl b x        ---> kill panel 


ctrl b w <--- ves todas las sesiones y todas las ventanas y te permite moverte inside 

---






---

s e c u r i t y 


s h a d o w 
donde se define el metodo de encyptacion del shadow :

~ ❯ cat /etc/login.defs| grep -i encrypt_method
ENCRYPT_METHOD YESCRYPT

~ > cat /etc/shadow                                          
root:$y$j9T$r2WpoGEI6tKS6 <--------------------- 

---






examen:





la de iterar con xargs 
xargs -I {} printf "value = %s\n" {} <g 