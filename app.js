//código novo

DELAY = 400;
var onOff = false;
var idx = 0;
var toques = [];
var arrayExpected = [];
var arrayPlayed = [];

$(document).ready(function () {
    setupAudio();

    $(".btn-on-off").click(function () {
        turnOnOff();
    });

    $(".btn-start").click(function () {
        start();
    });
    
    $(".btn-mute").click(function() {
        audioOnOff = !audioOnOff;
        $(this).find("img").attr("src", audioOnOff ? "img/btn_sound_on.png" : "img/btn_sound_off.png");
    });

    $(".btn").click(function () {
        if (!onOff || toques.length <= 0)
            return;

        // capta a cor clicada e toca o som
        var corClicada = $(this).data("cor");
        // valida sequencia
        if (toques[idx] != corClicada) {
            setTimeout(lose, DELAY);
            return;
        }

        console.log("arrayExpected: " + arrayExpected);//ids
        console.log(toques);
        d = new Date();
        console.log(d.toLocaleString());//userArrayLog.push(d.toLocaleString());

        // pisca cor corrente
        pisca($(this), 0);
        // anda na sequencia
        idx++;
        // se tudo ok, vai pra próxima rodada
        if (idx == toques.length)
            setTimeout(proximaJogada, DELAY);
    });
});

function zeraEstado() {
    // zera estado do jogo
    idx = 0;
    toques = [];
}

function turnOnOff() {
    zeraEstado();
    onOff = !onOff;
    $(".jogadas").html(onOff ? "000" : "");
    if (onOff) {
        $(".btn").sort(function (a, b) {
            return $(a).data("cor") - $(b).data("cor");
        }).each(function (i, o) {
            pisca($(o), DELAY * (i + 1));
        });
    }
}

function start() {
    zeraEstado();
    // inicia jogada
    proximaJogada();
}

function lose() {
    // guarda o score para animação
    $(".jogadas").data("score", lpad(toques.length, 3, '0'));
    
    //Enviar jogadas(toques) para app.

    zeraEstado();
    $(".jogadas").html("FAIL");
    playLose();
    animaLose();
}

function animaLose() {
    if (!onOff || toques.length > 0)
        return;
    j = $(".jogadas");
    j.html(j.html() == "FAIL" ? j.data("score") : "FAIL");
    setTimeout(animaLose, DELAY * 2);
}

function proximaJogada() {
    if (!onOff)
        return;

    // zera sequencia
    idx = 0;
    // insere nova cor aleatória
    toques.push(Math.floor(Math.random() * 4));
    // toca sons na sequencia
    for (i = 0; i < toques.length; i++) {
        var v = toques[i];
        pisca($(".btn[data-cor=" + v + "]"), DELAY * (i + 1));
    }
    arrayExpected.push($(".btn[data-cor=" + toques[toques.length-1] + "]").data("ncor"));
    // mostra jogada corrente
    $(".jogadas").html(lpad(toques.length, 3, '0'));
}

function pisca(o, delay) {
    setTimeout(function () {
        playCor($(o).data("cor"));
        $(o).find("img").fadeIn(24, function () {
            $(this).fadeOut();
        });
    }, delay);
}
function lpad(a, b, c) { a = a.toString(); for (i = a.length + 1; i <= b; i++) a = c + a; return a }