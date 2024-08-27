# Sistema de Reservas do Restaurante

### Este é um simples sistema de reservas em Python para um restaurante, que permite aos usuários fazer novas reservas, consultar reservas existentes ou cancelar reservas. O código foi desenvolvido para ser usado em um ambiente de terminal/console.

## Funcionalidades
+ Fazer uma Nova Reserva: O sistema permite que o usuário insira seu nome, data, horário e o número de pessoas para criar uma nova reserva.
+ Consultar uma Reserva Existente: O usuário pode consultar uma reserva existente, fornecendo seu nome.
+ Cancelar uma Reserva: O sistema permite ao usuário cancelar uma reserva existente, fornecendo seu nome.

## Pré-requisitos
Para executar este sistema, você precisará de:

+ Python 3.x instalado em sua máquina.
+ Um terminal ou prompt de comando para executar o script.

## Como Executar
+ Clone este repositório ou faça o download do código.

+ Navegue até o diretório onde o arquivo está localizado.
  
+ Execute o script usando o comando:
```python
python sistema_reservas_restaurante.py
```

O sistema solicitará que você escolha uma das opções:

+ 1: Fazer uma nova reserva.

+ 2: Consultar uma reserva existente.

+ 3: Cancelar uma reserva.

## Exemplos de Uso
### Fazer uma Nova Reserva
Ao escolher a opção 1, o sistema pedirá que você forneça os seguintes dados:

+ Nome
+ Data da reserva (no formato dd/mm/aaaa)
+ Horário da reserva (no formato hh:mm)
+ Quantidade de pessoas

Após a entrada, o sistema confirmará a reserva.

Exemplo:

```python
Você escolheu fazer uma nova reserva.
Por favor, informe os seguintes detalhes:
Digite seu nome: João Silva
Digite a data da reserva (dd/mm/aaaa): 25/08/2024
Digite o horário da reserva (hh:mm): 19:30
Quantidade de pessoas: 4
Reserva feita com sucesso para João Silva no dia 25/08/2024 às 19:30 para 4 pessoas.
```

### Consultar uma Reserva Existente
Ao escolher a opção 2, o sistema pedirá que você insira seu nome para consultar a reserva. O sistema exibirá uma reserva simulada.

Exemplo:
```python
Você escolheu consultar uma reserva existente.
Digite seu nome para consulta: João Silva
Reserva encontrada: João Silva, 25/08/2024 às 19:30 para 4 pessoas.
```
### Cancelar uma Reserva
Ao escolher a opção 3, o sistema pedirá que você insira seu nome para cancelar a reserva. O sistema simulará o cancelamento da reserva.

Exemplo:
```python
Você escolheu cancelar uma reserva.
Digite seu nome para cancelar a reserva: João Silva
Reserva para João Silva cancelada com sucesso.
```
## Estrutura do Código
O código está organizado em uma função principal chamada main(), que controla o fluxo do programa e gerencia as diferentes opções. Dependendo da escolha do usuário, ele pode:

+ Fazer uma nova reserva (Opção 1)
+ Consultar uma reserva existente (Opção 2)
+ Cancelar uma reserva existente (Opção 3)
  
Cada opção contém inputs específicos para capturar as informações necessárias e, posteriormente, fornece uma resposta adequada ao usuário.

## Futuras Melhorias
Algumas melhorias que podem ser implementadas no futuro:

+ Persistência de Dados: Armazenar as reservas em um banco de dados ou arquivo para que o sistema possa manipular dados reais em vez de simular.
+ Validação de Entrada: Adicionar validações para garantir que os dados de entrada (como data, hora e número de pessoas) estejam no formato correto.
+ Integração com APIs: Implementar uma integração com APIs externas para permitir reservas online em tempo real.
+ Interface Gráfica: Implementar uma interface gráfica (GUI) usando bibliotecas como Tkinter ou PyQt para tornar o sistema mais amigável.
## Contribuindo
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
