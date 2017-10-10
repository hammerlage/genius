//código novo

DELAY = 400;
var onOff = false;
var idx = 0;
var toques = [];
var arrayExpected = [];
var arrayPlayed = [];

var currRecord = {};
var data = [];
var blockGame = true;
var DATETIME_FORMAT = "YYYY-MM-DD HH:mm:ss:mmmm";

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

    $(".btn").click(function (event) {
		
		var currDateTime = new Date();
		var clickTimestamp = event.timeStamp;
		
        if (!onOff || toques.length <= 0 || blockGame)
            return;

		currRecord.clickTimeAt = currDateTime;
		var dataRecord = {
			userName: currRecord.userName
			, gameId: currRecord.gameId
			, roundChallenge: currRecord.roundChallenge.slice()
			, roundStartAt: moment(currRecord.roundStartAt).format(DATETIME_FORMAT)
			, roundStartTimestamp: currRecord.roundStartTimestamp
			, clickTimeAt: moment(currRecord.clickTimeAt).format(DATETIME_FORMAT)
			, clickTimestamp: clickTimestamp
			, roundSuccess: true
		};
		data.push(dataRecord);
		
        // capta a cor clicada e toca o som
        var corClicada = $(this).data("cor");
		
		dataRecord.currClickAnswer = arrayExpected.slice(0, idx);
		dataRecord.currClickAnswer.push($(".btn[data-cor=" + corClicada + "]").data("ncor"));
		
        // valida sequencia
        if (toques[idx] != corClicada) {
			
			for(var i = 0 ; i < data.length ; ++i){
				var item = data[i];
				if(item.gameId == currRecord.gameId && item.roundChallenge.length == currRecord.roundChallenge.length)
					item.roundSuccess = false;
			}
						
            setTimeout(lose, DELAY);
            return;
        }

        //console.log("arrayExpected: " + arrayExpected);//ids
        //console.log(toques);
        d = new Date();
        //console.log(d.toLocaleString());//userArrayLog.push(d.toLocaleString());

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
	arrayExpected = [];
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
	
	currRecord = {};
	currRecord.userName = null;
	currRecord.gameId = guid();
	
    // inicia jogada
    proximaJogada();
}

function lose() {
	
	//Enviar jogadas(toques) para app.
	var tempData = data.slice();
	data = [];
	submitGameData(tempData);
	
    // guarda o score para animação
    $(".jogadas").data("score", lpad(toques.length, 3, '0'));
    	
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

	blockGame = true;
	
    // zera sequencia
    idx = 0;
    // insere nova cor aleatória
    toques.push(Math.floor(Math.random() * 4));
    // toca sons na sequencia
    for (i = 0; i < toques.length; i++) {
        var v = toques[i];
        pisca($(".btn[data-cor=" + v + "]"), DELAY * (i + 1), i == (toques.length -1));
    }
    arrayExpected.push($(".btn[data-cor=" + toques[toques.length-1] + "]").data("ncor"));
	currRecord.roundChallenge = arrayExpected;
	
    // mostra jogada corrente
    $(".jogadas").html(lpad(toques.length, 3, '0'));
}

function pisca(o, delay, last) {
    setTimeout(function () {
        playCor($(o).data("cor"));
        $(o).find("img").fadeIn(24, function () {
            $(this).fadeOut();
        });
		
		if(last){
			blockGame = false;
			currRecord.roundStartAt = new Date();
			currRecord.roundStartTimestamp = performance.now();
		}
		
    }, delay);
}
function lpad(a, b, c) { a = a.toString(); for (i = a.length + 1; i <= b; i++) a = c + a; return a }

function guid() {
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
    s4() + '-' + s4() + s4() + s4();
}

function s4() {
  return Math.floor((1 + Math.random()) * 0x10000)
    .toString(16)
    .substring(1);
}

function submitGameData(dataToSubmit){
	for(var i = 0; i < dataToSubmit.length; ++i){
		var currItem = dataToSubmit[i];
		/* $.ajax({
			url: 'https://genius-io-project.appspot.com/api/clicks'
			, crossDomain: true
			, type: 'POST'
			, headers: {
			   "content-type": "application/json"
			 }
			, data: JSON.stringify(currItem)
			, success: function (response) {
				console.log(response);
			}
			, error: function (response) {
				console.log(response);
			}
		}); */
		var settings = {
		 "async": true,
		 "crossDomain": true,
		 "url": "https://genius-io-project.appspot.com/api/clicks",
		 "method": "POST",
		 headers: {
		   "content-type": "application/json",
		   "cache-control": "no-cache"
		 },
		 "processData": false,
		 "data": JSON.stringify(currItem)
		}

		$.ajax(settings).done(function (response) {
		 console.log(response);
		});
	}
}