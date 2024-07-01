from datetime import datetime

def estacao_do_ano(data):
    data = datetime.strptime(data, '%d/%m')
    
    verao_inicio1 = datetime(data.year, 12, 22)
    verao_inicio2 = datetime(data.year, 1, 1)
    outono_inicio = datetime(data.year, 3, 20)
    inverno_inicio = datetime(data.year, 6, 21)
    primavera_inicio = datetime(data.year, 9, 22)

    verao_final1 = datetime(data.year, 12, 31)
    verao_final2 = datetime(data.year, 3, 20)
    outono_final = datetime(data.year, 6, 21)
    inverno_final = datetime(data.year, 9, 23)
    primavera_final = datetime(data.year, 12, 22)

    
    if data >= verao_inicio1 and data < verao_final1:
        return 'Verão'
    elif data >= verao_inicio2 and data < verao_final2:
        return 'Verão'
    elif data >= outono_inicio and data < outono_final:
        return 'Outono'
    elif data >= inverno_inicio and data < inverno_final:
        return 'Inverno'
    elif data >= primavera_inicio or data < primavera_final:
        return 'Primavera'
    else:
        return 'Data inválida'

data_desejada = input("Digite a data desejada (formato dd/mm): ")
estacao = estacao_do_ano(data_desejada)
print(f"A estação do ano para a data {data_desejada} é: {estacao}")
