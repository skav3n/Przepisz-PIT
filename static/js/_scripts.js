function displayOn() {
	var numberOfPits, theWay, numberOfPitsWife;
	numberOfPits = document.getElementById("numberPits").value;
    theWay = document.getElementById("way").value;
	numberOfPitsWife = document.getElementById("numberPitsWife").value;

	if ( parseInt( numberOfPits ) >= 1 ) {
		document.getElementById("tabelka").style.display = "none";
		document.getElementById("buttonToAction").style.display = "inline";
		document.getElementById("pit11numberOne").style.display = "inline";
	}
	if ( parseInt( numberOfPits ) >= 2 ) {
		document.getElementById("pit11NumberTwo").style.display = "inline";
	}
	if ( parseInt( numberOfPits ) >= 3 ) {
		document.getElementById("pit11NumberThree").style.display = "inline";
	}
	if ( theWay == "wspolnie" || theWay == "wspolnie2" ) {
		if ( parseInt( numberOfPitsWife ) >= 1 ) {
			document.getElementById("pit11NumberOneWife").style.display = "inline";
		}
		if ( parseInt( numberOfPitsWife ) >= 2 ) {
			document.getElementById("pit11NumberTwoWife").style.display = "inline";
		}
		if ( parseInt( numberOfPitsWife ) >= 3 ) {
			document.getElementById("pit11NumberThreeWife").style.display = "inline";
		}
	}
}