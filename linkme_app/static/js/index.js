var inputS = document.getElementById('source');
var inputT = document.getElementById('target');
var body = document.getElementById('index');

var lightS = false;
var lightT = false;

inputS.addEventListener('click', function() {

	lightS = true;
	inputS.setAttribute('class', 'onclick');
	inputS.setAttribute('style', 'width: 89px; background-color: transparent;');
	inputS.setAttribute('placeholder', 'eg.: lower-url/');
});

inputT.addEventListener('click', function() {

	lightT = true;
	inputT.setAttribute('class', 'onclick');
 	inputT.setAttribute('style', 'width: 385px; background-color: transparent;');
	inputT.setAttribute('placeholder', 'eg.: www.my-ultra-site.com.br/50characters-maximum.html');
});

body.addEventListener('click', function() {
	console.log('aae');
	if (!lightS && inputS.value==""){
		inputS.setAttribute('class', 'input-container');
		inputS.setAttribute('style', 'width: 68px; background-color: transparent;');
		inputS.setAttribute('placeholder', '<base_dir>');
	}

	if (!lightT && inputT.value==""){
		inputT.setAttribute('class', 'input-container');
		inputT.setAttribute('style', 'width: 74px; background-color: transparent;');
		inputT.setAttribute('placeholder', '<target_url>');
	}
	//como os dois eventos sao executados qnd o input é ativado, o semaforo so eh apagado aqui
	lightS = false;
	lightT = false;
});