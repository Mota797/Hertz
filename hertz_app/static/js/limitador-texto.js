let nomes_produtos = []
let nome_produto = document.getElementsByClassName('nome-produto')

function adicionarTresPontos(){
    for (nome => nome_produto in nome_produto){
        nomes_produtos.push(nome)

        if (nomes_produtos[i].innerText.length > 19){
            nomes_produtos[i].styles.cssText('color: red')
        }
        i++
    }
        
    console.log(texto_produto.innerText)
}

adicionarTresPontos()