let word = document.querySelector('#word')
let btn = document.querySelector('#btn')
let offset = document.querySelector('#offset')

let alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
alphabet=alphabet.join('').toLowerCase()
let newString= ''

 
btn.onclick = function() {
    for (let i = 0; i < word.value.length; i++){  

        let index_of_english_words = alphabet.indexOf(word.value[i])
        console.log(index_of_english_words)
        // console.log(parseInt(index_of_english_words) + parseInt(offset.value))
        let offset_of_english = alphabet[(parseInt(index_of_english_words) + parseInt(offset.value)) % 26 ]
        newString+=offset_of_english
        let newWord=newString
        resultText.innerHTML = newWord
    }
   console.log(newString) 

   // place newString on the dom displaying it

   newString=''
}


