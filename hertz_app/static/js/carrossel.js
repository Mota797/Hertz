const botao_esquerda = document.getElementById('passar_esquerda');
const botao_direita = document.getElementById('passar_direita');

const imagem1 = document.getElementById('img_carrossel_produto1');
const imagem2 = document.getElementById('img_carrossel_produto2');
const imagem3 = document.getElementById('img_carrossel_produto3');

const lista_carrossel = document.getElementById('lista_carrossel_detalhe');
const array_carrossel = [imagem1, imagem2, imagem3]

let i = 0;

botao_esquerda.onclick = function () {
    if (i < array_carrossel.length && i != 0){
        i = i - 1
    }
    else if (i == 0){
        i = (array_carrossel.length - 1)
    }
    lista_carrossel.style.transform = `translateX(-${i * 100}%)`
    console.log('esquerda')
}

botao_direita.onclick = function () {
    if (i == (array_carrossel.length - 1)){
        i = 0
    }

    else if (i <= (array_carrossel.length - 1)) {
        i += 1
    }

    lista_carrossel.style.transform = `translateX(-${i * 100}%)`
    console.log('direita')
}