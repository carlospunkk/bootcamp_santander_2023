
verifica()

function verifica(){
  var palavra = "casa"

  var separaletras = palavra.split("")
  
  var palavrainvertida = separaletras.reverse() 
  
  palavrainvertida = palavrainvertida.join("") 

  if(palavra === palavrainvertida){
    console.log("é um palindromo")
  }else{
    console.log("não um palindromo")
  }

}


