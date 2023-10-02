#minha copia e ja tive um bug

import ipaddress

def calculadora_ip():
    
    while True:
        print('\nCalculadora de IP')
        print('1. Calcular Mascara de Sub-rede')
        print('2. Identificar endereco de rede')
        print('3. Verificar se dois Ips estao na mesma Rede')
        print('4. Sair')

        escolha = input('Escolha uma opcao (1/2/3/4): ')

        if escolha == '1':
            ip = input('Digite o endereco IP: ')
            prefixo = int(input('Digite o prefixo da mascara de sub-rede: '))
            rede = ipaddress.IPv4Network(f'{ip}/{prefixo}', strict=False)
            print(f'Mascara de Sub-rede: {rede.netmask}')

        elif escolha == '2':
            ip = input('Digite o endereco IP: ')
            prefixo = int(input('Digite o prefixo da mascara de sub-rede: '))
            rede = ipaddress.IPv4Network(f'{ip}/{prefixo}', strict=False)
            print(f'Endereco de rede: {rede.network_address}')

        elif escolha == '3':
            ip1 = input('Digite o primeiro endereco IP: ')
            ip2 = input('Digite o segundo endereco IP: ')
            prefixo = int(input('Digite o prefixo da mascara de rede: '))
            rede1 = ipaddress.IPv4Network(f'{ip1}/{prefixo}', strict=False)
            rede2 = ipaddress.IPv4Network(f'{ip2}/{prefixo}', strict=False)
            if rede1.network_address == rede2.network_address:
                print('Os Ips estao na mesma rede')
            else:
                print('Os Ips nao estao na mesma rede')

                break

        else:
            print('Opcao Invalida. Tente novamente.')


if __name__ == '__main__':
    calculadora_ip()
