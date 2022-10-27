const cards = {
    "a":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":10,
    "Q":10,
    "K":10,
    "A":11
}
values = [1,2,3,4,5,6,7,8,9,10]

function randoms(i){
    return i[Math.floor(Math.random()*i.length)]
}

let winnings = ''
var ace = 0 
let dealer = document.querySelector('#dealer')
let hit = document.querySelector('#hit')
let stay = document.querySelector('#stay')

play.onclick = function(){

    let generated = document.querySelector('#generated')
    
    var cardValue1 = 0
    var cardValue2 = 0

    for (let i=0; i<1; i++){
        var cardValue1 = 1
        var cardValue2 = randoms(values)
        var dealer1 = randoms(values)
        var dealer2 = randoms(values)}
    if (cardValue1 == 1){
        generated.innerHTML = "Submit a 1 or 11 for your first card"
    }
    else if (cardValue2 == 1){
        generated.innerHTML = "Submit a 1 or 11 for your first card"
    }
    else {
    console.log(cardValue1)
    console.log(cardValue2)}}
ace.onclick =function(){
    ace=11
}
hit.onclick = function(){
    console.log(cardValue1)
    console.log(cardValue2)
    var total_value = cardValue1+cardValue2
    console.log(total_value)
    for (let i=0; i<5; i++){
        var cardValue = randoms(values)
        total_value += cardValue
        i+1
console.log(total_value)}}

/*
if (cardValue1 = 1){
    ace_submit.innerHTML = (`Got an Ace and a ${cardValue2} - Submit 1 or 11`)
    ace_submit.onclick = function(){
        cardValue1 = ace.value
        console.log(`Got a ${cardValue1} and a ${cardValue2} - That's a total of ${cardValue1+=cardValue2}`)}
    }
else if (cardValue1 = 11){
    ace_submit.innerHTML = (`Got an Ace and a ${cardValue2} - Submit 1 or 11`)
    ace_submit.onclick = function(){
        cardValue1 = ace.value
        console.log(`Got a ${cardValue1} and a ${cardValue2} - That's a total of ${cardValue1+cardValue2}`)}
    }
}
*/