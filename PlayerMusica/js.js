
let Musicas = [];

function addmusica(nome){
    var musica = new Audio(nome);
    Musicas.push(musica);

    document.getElementById('nomemusica').innerHTML = nome.replace('.mp3','').replace('./addons/','');
}

addmusica('./addons/transgender.mp3');



function minseg(total){
    var totalmin = parseInt(parseInt(total)/60);
    var totalseg =  parseInt(total - parseInt(totalmin)*60);



    
    if(totalmin < 10){
        totalmin = '0'+parseInt(totalmin); 
    }
    if(totalseg < 10){
        totalseg = '0'+parseInt(totalseg);
    }


    return  totalmin+':'+totalseg;

}



function tempos(){

    var onde = document.getElementById('atualtmp');
    var barra = document.getElementById('andar');

    var tempoatual = Musicas[0].currentTime;



    var conta = 100*tempoatual/Musicas[0].duration;


    barra.style.width = conta+'%'
    
    onde.innerHTML= minseg(tempoatual);

}








function mostrar(){
    var teste = document.getElementById('eiei');
    var tela = window.innerWidth;

    if(parseInt(tela) < 420){
        teste.style.width  = '100%';

    }else{
        teste.style.width  = '40%';
    };

}

mostrar()





function pausadespausa(){
    var lugar = document.getElementById('play-pause');

    if(lugar.classList.contains('pausado')){
        lugar.classList.remove('pausado');
        lugar.classList.add('tocando');

        lugar.innerHTML= '<img src="./addons/pausa.png" onclick="pausadespausa()">'

        Musicas[0].play()
    }else if(lugar.classList.contains('tocando')){
        lugar.classList.remove('tocando');
        lugar.classList.add('pausado');

        lugar.innerHTML= '<img src="./addons/play.png" onclick="pausadespausa()">'

        Musicas[0].pause()

    }



}













setInterval(mostrar,500);
setInterval(tempos,500)

