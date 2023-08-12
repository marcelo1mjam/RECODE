// EVENTOS onclick = disparado quando o usuário clica sobre o elemento.
// onchange = disparado quando um elemento HTML foi alterado.
//onmouseover = disparado quando o usuário passa o mouse porcima do elemento.
// onmouseout = disparado quando o usuário movimenta o mouse para fora do elemento.
// onkeydown = disparado quando o usuário pressiona alguma tecla no teclado.
//onload = disparado quando o navegador termina de carregar uma página.


function EventoDeScroll() {
    console.log('rollando na função');
    
}

document.onscroll = EventoDeScroll;

let EventoDeScrollComSeta = ()=> {
    console.log('Função com seta')
}