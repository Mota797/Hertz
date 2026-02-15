const botao_esquerda = document.getElementById('passar_esquerda');
const botao_direita = document.getElementById('passar_direita');

// const imagem1 = document.getElementById('img_carrossel_produto1');
// const imagem2 = document.getElementById('img_carrossel_produto2');
// const imagem3 = document.getElementById('img_carrossel_produto3');

const lista_carrossel = [document.getElementById('img_carrossel_produto1'), document.getElementById('img_carrossel_produto2'), document.getElementById('img_carrossel_produto3')];

let i = 0;

botao_esquerda.onclick = function () {

    lista_carrossel[i].style.transform = 'translateX(0%)'
    if (i < lista_carrossel.length && i != 0){
        i -= 1
    }
    else if (i == 0){
        i = (lista_carrossel.length - 1)
    }
    
    lista_carrossel[i].style.transform = `translateX(calc(${i} * 100%))`
    console.log(i)
}

botao_direita.onclick = function () {
    console.log(lista_carrossel[i])
    lista_carrossel[i].style.transform = 'translateX(0%)'
    if (i == (lista_carrossel.length - 1)){
        i = 0
        console.log(i)
    }

    else if (i <= (lista_carrossel.length - 1)) {
        i += 1
        console.log(i)
    }

    lista_carrossel[i].style.transform = `translateX(calc(${i} * -100%))`
    console.log(i)
}

console.log(i)