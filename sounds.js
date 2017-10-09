var audioOnOff = true;
var audioGreen = null;
var audioYellow = null;
var audioBlue = null;
var audioRed = null;
var audioLose = null;

function setupAudio() {
	if (!window.HTMLAudioElement)
		return;

    audioGreen = loadAudio('sounds/simonSound1.mp3');
    audioYellow = loadAudio('sounds/simonSound3.mp3');
    audioBlue = loadAudio('sounds/simonSound4.mp3');
    audioRed = loadAudio('sounds/simonSound2.mp3');
    audioLose = loadAudio('sounds/wrong.mp3');
}

function loadAudio(src) {
	if (!window.HTMLAudioElement)
		return null;

    var o = document.createElement('audio');
    o.setAttribute('src', src);
    o.load()
    return o;
}

function playAudio(o) {
    if (!audioOnOff)
        return;
        
    try {
        o.currentTime = 0;
    } catch(e) { }
    o.play();
}

function playLose() {
    playAudio(audioLose);
}

function playCor(idx) {
    switch (idx) {
        case 0:
            playAudio(audioGreen);
        break;
        case 1:
            playAudio(audioYellow);
        break;
        case 2:
            playAudio(audioBlue);
        break;
        case 3:
            playAudio(audioRed);
        break;
    }
}