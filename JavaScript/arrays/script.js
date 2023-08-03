var nome = ['carro', 'avião', 'bicicleta'];
console.log(nome);
console.log(typeof(nome));

var veiculo = Array('carro', 'avião', 'bicicleta');
console.log(veiculo);
console.log(typeof(veiculo));

console.log(veiculo[1]);
console.log(veiculo[2]);
veiculo[3] = "jato";

console.log(veiculo);
console.log(veiculo[3]);

veiculo.push('charrete');
console.log(veiculo);

let removido = veiculo.pop();
console.log(veiculo);
console.log(removido);

let = removido2 = veiculo.shift();
console.log(veiculo);
console.log(removido2);

veiculo.push('carro');
veiculo.push('charrete');

console.log(veiculo);
veiculo.sort();
console.log(veiculo);

console.log(veiculo.length);

for (let i=0; i<veiculo.length; i++){
    console.log(veiculo[i]);
}

let contador = 0;
while (contador < veiculo.length){
    console.log(veiculo[contador++]);
}

veiculo.map(function(n){
    console.log(n);
});