let firstCard = document.querySelector('#firstCard')
let secondCard = document.querySelector('#secondCard')
let thirdCard = document.querySelector('#thirdCard')
let btn = document.querySelector('#btn')



const cardValue = 
{"ace": 1, "king": 10, "queen": 10, "jack": 10, "1": 1, "2": 2, 
"3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

btn.onclick = function(){
    let card1 = firstCard.value
    let card2 = secondCard.value
    let card3 = thirdCard.value
    let total = cardValue[card1] + cardValue[card2] + cardValue[card3]
    let result = total
    
        if (total < 17){
            resultText.innerHTML = `${result} hit`
        } 
        else if(total >= 17 && total < 21 ){
            resultText.innerHTML = `${result} stay`
        }
        else if(total === 21){
            resultText.innerHTML = `${result} blackjack!`
        }   
        else{
            resultText.innerHTML = `${result} already busted`
        }

}
