def cadastro_cliente (): 
        
    nome = input("Digite seu nome:");
    idade = input("Digite sua idade:");
    cpf = input("Digite seu cpf:");
    endereco = input("Digite seu endereço:");
    pessoa = [];
    pessoa.append(nome);
    pessoa.append(idade);
    pessoa.append(cpf);
    pessoa.append(endereco);
    consulta = input("Deseja consultar cliente: ")

def cadastro_destino():
    destino = input("Digite a cidade de destino:");
    periodo = input("Digite os dias que passará no destino: ");
    data = input("Digite a data de saída para o destino:");

cadastro = int(input("Digite 1 para cadastrar cliente, 2 para cadastrar destino:"));

if (cadastro == 1):
    cadastro_cliente();
if (cadastro == 2):
    cadastro_destino();
consulta = int(input("Digite 3 para consultar cliente, 4 para consultar destino:"));

if (consulta == 3):
    print(pessoa);
if (consulta == 4):
    print(cadastro_destino);