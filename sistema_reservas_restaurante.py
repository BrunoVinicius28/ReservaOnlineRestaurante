def main():
    print("Bem-vindo ao sistema de reservas do Restaurante!")
    print("Por favor, selecione uma das opções abaixo:")
    print("1: Fazer uma nova reserva")
    print("2: Consultar uma reserva existente")
    print("3: Cancelar uma reserva")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        print("Você escolheu fazer uma nova reserva.")
        print("Por favor, informe os seguintes detalhes:")
        nome = input("Digite seu nome: ")
        data = input("Digite a data da reserva (dd/mm/aaaa): ")
        horario = input("Digite o horário da reserva (hh:mm): ")
        pessoas = input("Quantidade de pessoas: ")

        print(f"Reserva feita com sucesso para {nome} no dia {data} às {horario} para {pessoas} pessoas.")

    elif escolha == '2':
        print("Você escolheu consultar uma reserva existente.")
        nome = input("Digite seu nome para consulta: ")
        # Simulação de consulta a uma reserva
        print(f"Reserva encontrada: {nome}, 25/08/2024 às 19:30 para 4 pessoas.")

    elif escolha == '3':
        print("Você escolheu cancelar uma reserva.")
        nome = input("Digite seu nome para cancelar a reserva: ")
        # Simulação de cancelamento de reserva
        print(f"Reserva para {nome} cancelada com sucesso.")

    else:
        print("Opção inválida. Encerrando a conexão.")


if __name__ == "__main__":
    main()
