function howManyPit11() {
    var numberOfPits, numberOfPitsWife, pit, pitWife, number, numberWife, pit11Table, pit11TableWife;
    
	numberOfPits = document.getElementById("numberPits").value;
	numberOfPitsWife = document.getElementById("numberPitsWife").value;
    
    pit = document.getElementById( 'tabelaSkladki' );
    
    number = document.getElementById( 'numerPitaPodatnik' );
    numberWife = document.getElementById( 'numerPitaMalzonka' );
    
    pit11Table = document.getElementById("pit11platnik");
    pit11TableWife = document.getElementById("pit11malzonek");
    
    
    for ( var i = 0; i < parseInt( numberOfPits ) - 1; i++ ) {
        pit11Table.innerHTML += '<div id="pitNumer'+ i +'"></div>';
        
        pit11Table.children[i].appendChild( number.cloneNode( true ) );
        
        pit11Table.children[i].appendChild( pit.cloneNode( true ) );
    
        pit11Table.children[i].firstChild.children[0].textContent = i + 2;
        
        var numberOfInputs = pit11Table.children[i].getElementsByTagName('input').length;
        
        for ( var j = 0; j < numberOfInputs; j++ ) {
            var inputName = pit11Table.children[i].getElementsByTagName('input')[j].getAttribute( "name" );
            
            var newInputName = inputName.substr( 0, inputName.length - 1 ) + (i + 1);
            
            pit11Table.children[i].getElementsByClassName('inputs')[j].innerHTML = '<input type="text" name="' + newInputName +'" value="">';
        }
    }
    
    for ( var i = 0; i < parseInt( numberOfPitsWife - 1 ); i++ ) {
        pit11TableWife.innerHTML += '<div id="pitNumer'+ i +'"></div>';
        
        pit11TableWife.children[i].appendChild( numberWife.cloneNode( true ) );
        
        pit11TableWife.children[i].appendChild( pit.cloneNode( true ) );
    
        pit11TableWife.children[i].firstChild.children[0].textContent = i + 2;
        
        var numberOfInputsWife = pit11TableWife.children[i].getElementsByTagName('input').length;
        
        for ( var j = 0; j < numberOfInputsWife; j++ ) {
            var inputNameWife = pit11TableWife.children[i].getElementsByTagName('input')[j].getAttribute( "name" );
            
            var newInputNameWife = inputNameWife.substr( 0, inputNameWife.length - 2 ) + 'mp' + (i + 1);
            
            pit11TableWife.children[i].getElementsByClassName('inputs')[j].innerHTML = '<input type="text" name="' + newInputNameWife +'" value="">';
        }
    }
}