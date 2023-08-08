print("\nAgência Viagem dos Sonhos\n");
pessoa = [];
destino = [];


menu = int(input("Digite:\n 1 para cadastrar cliente\n 2 para cadastrar destino\n 3 para consultar cliente\n 4 para consultar destino\n 0 para sair:\n\n"));
while menu != 0:

    if menu == 1:
        nome = input("\nDigite seu nome:");
        idade = input("Digite sua idade:");
        cpf = input("Digite seu cpf:");
        endereco = input("Digite seu endereço:");
        print("Cliente cadastrado com sucesso!")
        
        
        pessoa.append(nome);
        pessoa.append(idade);
        pessoa.append(cpf);
        pessoa.append(endereco);
        menu = int(input("\n\nDigite:\n 1 para cadastrar cliente\n 2 para cadastrar destino\n 3 para consultar cliente\n 4 para consultar destino\n 0 para sair:\n\n"));
        

    elif menu == 2:
        cidade = input("Digite a cidade de destino:");
        periodo = input("Digite os dias disponíveis para o destino:");
        data = input("Digite a data de saída para o destino:");
        print("Destino cadastrado com sucesso!")

        destino.append(cidade);
        destino.append(periodo);
        destino.append(data);
        menu = int(input("\n\nDigite:\n 1 para cadastrar cliente\n 2 para cadastrar destino\n 3 para consultar cliente\n 4 para consultar destino\n 0 para sair:\n\n"));


    elif menu == 3:
        if menu == 3 and pessoa == []:
            print("\n\nNão há clientes cadastrados, por vafor cadastre pelo menos 1 cliente!");
            menu = int(input("\n\nDigite:\n 1 para cadastrar cliente\n 2 para cadastrar destino\n 3 para consultar cliente\n 4 para consultar destino\n 0 para sair:\n\n"));

        else:
        
            print(pessoa);     
            menu = int(input("\n\nDigite:\n 1 para cadastrar cliente\n 2 para cadastrar destino\n 3 para consultar cliente\n 4 para consultar destino\n 0 para sair:\n\n"));
    
    elif menu == 4:
        if menu == 4 and destino == []:
            print("\n\nNão há destinos cadastrados, por vafor cadastre pelo menos 1 destino!");
            menu = int(input("\n\nDigite:\n 1 para cadastrar cliente\n 2 para cadastrar destino\n 3 para consultar cliente\n 4 para consultar destino\n 0 para sair:\n\n"));
        else:
            print(destino);
            menu = int(input("\n\nDigite:\n 1 para cadastrar cliente\n 2 para cadastrar destino\n 3 para consultar cliente\n 4 para consultar destino\n 0 para sair:\n\n"));

"""

Agencia de viagens Sonhos

Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

3


Não há clientes cadastrados, por vafor cadastre pelo menos 1 cliente!


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

4


Não há destinos cadastrados, por vafor cadastre pelo menos 1 destino!


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

1

Digite seu nome:Marcelo
Digite sua idade:36
Digite seu cpf:123.453.456-34
Digite seu endereço:Rua Safira
Cliente cadastrado com sucesso!


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

3
['Marcelo', '36', '123.453.456-34', 'Rua Safira']


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

1

Digite seu nome:Sandro
Digite sua idade:65
Digite seu cpf:342.345.123-23
Digite seu endereço:Rua Carmo
Cliente cadastrado com sucesso!


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

3
['Marcelo', '36', '123.453.456-34', 'Rua Safira', 'Sandro', '65', '342.345.123-23', 'Rua Carmo']


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

2
Digite a cidade de destino:Belo Horizonte
Digite os dias disponíveis para o destino:4
Digite a data de saída para o destino:12/12/2023
Destino cadastrado com sucesso!


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

4
['Belo Horizonte', '4', '12/12/2023']


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

2
Digite a cidade de destino:Brasília
Digite os dias disponíveis para o destino:5
Digite a data de saída para o destino:23/04/2024
Destino cadastrado com sucesso!


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

4
['Belo Horizonte', '4', '12/12/2023', 'Brasília', '5', '23/04/2024']


Digite:
 1 para cadastrar cliente
 2 para cadastrar destino
 3 para consultar cliente
 4 para consultar destino
 0 para sair:

0

"""