
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<form action="javascript:register();">
	<label>Nom utilisateur:</label>
	<span id="user_name">Sylvain</span>
	<br>
	<br>
	<br>
	<label>E-mail:</label>
	<input id="user_email" class="field" type="email" value="" placeholder="E-Mail"/>

	<br>
	<br>
	<br>


	<label>Numéro de téléphone:</label>
	<input id="user_phone" class="field" type="tel" value="0606060606" />

	<br>
	<br>
	<br>

	<label>Mot de passe:</label>
	<input id="user_password" class="field" type="password" />

	<div class="success" style="display:none;">
		<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-emoji-smile" viewBox="0 0 16 16">
			<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
			<path d="M4.285 9.567a.5.5 0 0 1 .683.183A3.498 3.498 0 0 0 8 11.5a3.498 3.498 0 0 0 3.032-1.75.5.5 0 1 1 .866.5A4.498 4.498 0 0 1 8 12.5a4.498 4.498 0 0 1-3.898-2.25.5.5 0 0 1 .183-.683zM7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zm4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5z"/>
		</svg>
	</div>
	<div class="error" >
		<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-emoji-frown" viewBox="0 0 16 16">
			<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
			<path d="M4.285 12.433a.5.5 0 0 0 .683-.183A3.498 3.498 0 0 1 8 10.5c1.295 0 2.426.703 3.032 1.75a.5.5 0 0 0 .866-.5A4.498 4.498 0 0 0 8 9.5a4.5 4.5 0 0 0-3.898 2.25.5.5 0 0 0 .183.683zM7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zm4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5z"/>
		</svg>
	</div>

	<br>
	<br>
	<br>
	<input id="btn_register" type="submit" value="enregistrer" style="display:none;">
</form>

<button onclick="getUser(alert('coucou'));">Nom utilisateur</button>
<button id="btn_email">E-mail</button>
<button id="btn_phone">Téléphone</button>




<script>

$(document).ready(function() {

	$("#btn_email").on('click', getEmail);
	$("btn_phone").on('click', changePhone);
	$("user_password").on('keyup', checkPassword);
	$("").on('', changeField);

});

function getUser(){
	alert('aaa');
	alert($("#user_name").html());
	//Afficher dans un pop-up ou en console le nom de l'utilisateur

}

var getEmail = function() {

	//Afficher dans un pop-up ou en console la valeur du champ email


}

var changePhone = function() {

	//Changer la valeur du numéro de téléphone

}

var checkPassword = function() {

	//Vérifiez que le mot de passe à plus de 8 caractères

}
// Création d'un fonction qui appel checkData() à chaque changement d'un champ


function checkData(){

	//Vérification Mot de passe Ok et l'email non vide

}

function register(){

	alert("Bravo !");

}

</script>