let botao_um = document.getElementById('botao_play_um');
let botao_dois = document.getElementById('botao_play_dois');
let botao_tres = document.getElementById('botao_play_tres');
let audio_um = document.getElementById('audio_um');
let audio_dois = document.getElementById('audio_dois');
let audio_tres = document.getElementById('audio_tres');

botao_um.addEventListener('click', () => {
    audio_um.play()
    }
)

botao_dois.addEventListener('click', () => {
    audio_dois.play()
    }
)

botao_tres.addEventListener('click', () => {
    audio_tres.play()
    }
)

