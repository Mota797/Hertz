const estrelas = document.querySelectorAll('.estrelas span');
const inputNota = document.querySelector('input[name="nota_avaliacao"]');

estrelas.forEach(estrela => {
    estrela.addEventListener('click', function() {
        const valor = this.dataset.value;

        inputNota.value = valor;

        estrelas.forEach(e => {
            e.classList.remove('ativa');
        });

        for (let i = 0; i < valor; i++) {
            estrelas[i].classList.add('ativa');
        }
    });
});