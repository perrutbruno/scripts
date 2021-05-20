import socket
import ssl, datetime

def ssl_check(hostname):
    ssl_date_fmt = r'%d %b %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    #timeout de 3 segundos devido a limitacoes do lambda
    conn.settimeout(3.0)

    try:
        conn.connect((hostname, 443))
        ssl_info = conn.getpeercert()
        # parse na string do certificado em um objeto python datetime
        #return datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        return ssl_info
    except Exception as e:
        pass


def read_logfile(archive):
    ''' Read all dns registers separated by \n each register inside a txt file and containing a blank line as file's last line '''
    list_w_domains = []
    # Abrir o arquivo com permissao de SomenteLeitura
    f = open(archive, "r")
    # usa readlines para ler todas as linhas do arquivo
    # a variavel "lines" eh uma variavel contendo todas as linhas do arquivo
    lines = f.readlines()
    # fecha o arquivo.
    f.close()
    for line in lines:
        list_w_domains.append(line[:-1])

    return list_w_domains

#arquivo que contem os subdominios
all_registers = read_logfile('lista-dominios')

for register in all_registers:
    #print(register)
    try:
        check = ssl_check(register)
        check_commonName = check['subject'][-1]
        # !!!! CASO ALTERE O SUBDOMINIO, ALTERAR LINHA ABAIXO!
        if check_commonName == (('commonName', '*.YOURDOMAIN.com.br'),):
            exp_date = check['notAfter']
            CA = check['issuer'][-1][-1][-1]

            f = open("logs.txt", "a")
            f.write(f"Registro {register} com data de expiracao {exp_date} e CA {CA}! \n")
            f.close()
    except Exception as key:
        print(f"Registro {register} com certificado com problemas! \n")


