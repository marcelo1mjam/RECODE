//window.innerWidth controle da largurada página
//screen.width controle da resolução
//window.onresize quando houver ajuste de tamanho
console.log(window.innerWidth);
console.log(screen.width);

// Imprime o tamanho da tela toda vez que houver mudança na largura da página
window.onresize = function(){
    console.log(window.innerWidth);
}

var numero = "18";
console.log(typeof(numero));

// onload quando a tela for carregada

document.getElementsByTagName("img"); // pega todas as tags img.
//document.getElementsByTagName("div")[10].style = "color:blue" pega a div[10] e modifica o estilo para cor azul
document.onscroll = function(){
    console.log("rolando...");
}
