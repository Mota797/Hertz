const container_estrelas = document.querySelectorAll('div.container-estrelas');

function adicionar_estrelas() {
    container_estrelas.forEach(container => {
        
        const nota_avaliacao = Number(container.dataset.nota);
        const linha_estrelas = document.createElement('div');
        linha_estrelas.classList.add('linha-estrela');

        for (let i = 0; i < 5; i++) {
            if (i < nota_avaliacao) {
                linha_estrelas.innerHTML += `<i class="fa-solid fa-star"></i>`;
            } else {
                linha_estrelas.innerHTML += `<i class="fa-regular fa-star"></i>`;
            }
        }

        container.appendChild(linha_estrelas);
    });
}

adicionar_estrelas();
