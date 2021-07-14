function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function getQuery() {
    var query = getParameterByName('q');
    console.log('Query: ' + query);
    if (query == 'a') {
        document.getElementById('left').style.animation='none';
        document.getElementById('right').style.animation='none';
        document.getElementById('box').style.animation='none';
        document.getElementById('box').style.width='480px';
        document.getElementById('box').style.height='240px';
        document.getElementById('box').style.boxShadow='40px 40px 40px #cccccc, 0 0 0 #ffffff, 0 0 0 #cccccc inset, 2px 2px 2px #ffffff inset';
        document.getElementById('box').style.background='#fafafa';
    }
    else {
        return false;
    }
}