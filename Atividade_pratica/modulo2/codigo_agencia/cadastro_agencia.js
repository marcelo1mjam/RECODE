
    const clientes = [];
    
    function cadastrarCliente() {

        const cliente = {};
    
        const nome = document.getElementById("Nome").value;
        const idade = document.getElementById("Idade").value;
        const cpf = document.getElementById("CPF").value;
        const endereco = document.getElementById("Endereco").value;

        cliente.Nome = nome;
        cliente.Idade = idade;
        cliente.CPF = cpf;
        cliente.Endereço = endereco;

        clientes.push(cliente); 
        
        document.getElementById("Nome").value = "";
        document.getElementById("Idade").value = "";
        document.getElementById("CPF").value = "";
        document.getElementById("Endereco").value = "";

    }

   

    function consultarCliente(){
        const resultadoElement = document.getElementById("resultado");
        resultadoElement.innerText = JSON.stringify(clientes, null, 2);
    }
  
    

    const destinos = [];
    
    function cadastrarDestino() {

        const destino = {};
    
        const cidade = document.getElementById("Cidade").value;
        const periodo = document.getElementById("Periodo").value;
        const data = document.getElementById("Data").value;
       

        destino.Cidade = cidade;
        destino.Período = periodo;
        destino.Data = data;
        

        destinos.push(destino); 
        
        document.getElementById("Cidade").value = "";
        document.getElementById("Periodo").value = "";
        document.getElementById("Data").value = "";
        

    }

   

    function consultarDestino(){
        const resultadoElement = document.getElementById("resultado");
        resultadoElement.innerText = JSON.stringify(destinos, null, 2);
    }
  
    
