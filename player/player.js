function playVideo(videoId) {
    document.getElementById('player').src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
    document.getElementById('playerContainer').style.display = 'flex';
}
function pauseVideo() {
    document.getElementById('player').contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
}
function resumeVideo() {
    document.getElementById('player').contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
}
