#minha copia e ja tive um bug

import ipaddress

def calculadora_ip():
    while True:
        print("\nCalculadora de IP")
        print("1. Calcular Máscara de Sub-rede")
        print("2. Identificar Endereço de Rede")
        print("3. Verificar se Dois IPs estão na Mesma Rede")
        print("4. Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == '1':
            ip = input("Digite um endereço IP: ")
            prefixo = int(input("Digite o prefixo da máscara de sub-rede (exemplo: 24): "))
            rede = ipaddress.IPv4Network(f"{ip}/{prefixo}", strict=False)
            print(f"Máscara de Sub-rede: {rede.netmask}")
        elif escolha == '2':
            ip = input("Digite um endereço IP: ")
            prefixo = int(input("Digite o prefixo da máscara de sub-rede (exemplo: 24): "))
            rede = ipaddress.IPv4Network(f"{ip}/{prefixo}", strict=False)
            print(f"Endereço de Rede: {rede.network_address}")
        elif escolha == '3':
            ip1 = input("Digite o primeiro endereço IP: ")
            ip2 = input("Digite o segundo endereço IP: ")
            prefixo = int(input("Digite o prefixo da máscara de sub-rede (exemplo: 24): "))
            rede1 = ipaddress.IPv4Network(f"{ip1}/{prefixo}", strict=False)
            rede2 = ipaddress.IPv4Network(f"{ip2}/{prefixo}", strict=False)
            if rede1.network_address == rede2.network_address:
                print("Os IPs estão na mesma rede.")
            else:
                print("Os IPs não estão na mesma rede.")
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora_ip()
