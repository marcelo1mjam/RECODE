// IF ELSE

let numero = 5;

if (numero == 1)
    console.log("INICIAR");
else if ( numero == 2)
    console.log("PAUSAR");
else if (numero == 3)
    console.log("AVANÇAR");
else if (numero == 4)
    console.log("RETROCEDER");
else if (numero == 5)
    console.log("DESLIGAR");
else 
    console.log("Comando inválido");


// SWITCH

switch (numero){
    case 1:
        console.log("INICIAR");
        break;
    case 2:
        console.log("PAUSAR");
        break;
    case 1:
        console.log("AVANÇAR");
        break;
    case 1:
        console.log("RETROCEDER");
        break;
    case 1:
        console.log("DESLIGAR");
        break;
    default:
        console.log("Comando inválido");
}


let mes = 5;

if ( mes >= 1 && mes <= 3)
    console.log("primeiro trimestre");
else if ( mes >= 4 && mes <= 6)
    console.log("segundo trimestre");
else if ( mes >= 7 && mes <= 9)
    console.log("terceiro trimestre");
else if ( mes >= 10 && mes <= 12)
    console.log("quarto trimestre");
else 
    console.log("Mês inválido");


switch (mes){
    case 1:
    case 2:
    case 3:
        console.log("primeiro trimestre");
        break;
    case 4:
    case 5:
    case 6:
        console.log("segundo trimestre");
        break;
    case 7:
    case 8:
    case 9:
        console.log("terceiro semestre");
        break;
    case 10:
    case 11:
    case 12:
        console.log("quarto trimestre");
        break;
    default:
        console.log("mes inválido");
}



