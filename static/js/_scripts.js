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
	if ( theWay == "2" || theWay == "3" ) {
		if ( parseInt( numberOfPitsWife ) >= 1 ) {
			document.getElementById("pit11NumberOneWife").style.display = "inline";
			document.getElementById("pit11malzonek").style.display = "inline";
		}
	}
}

function printDiv(divName) {
     var printContents = document.getElementById(divName).innerHTML;
     var originalContents = document.body.innerHTML;

     document.body.innerHTML = printContents;

     window.print();

     document.body.innerHTML = originalContents;
}

