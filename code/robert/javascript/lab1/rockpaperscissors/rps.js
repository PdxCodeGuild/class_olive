var options = [
    "rock",
    "paper",
    "scissors"
];

var randomOptions = options[Math.floor(Math.random()*options.length)]
//result = (randomOptions)//test

let w = 0
let l = 0
let d = 0

let p = document.querySelector('#p')
let r = document.querySelector('#r')
let s = document.querySelector('#s')
let stats = ''
let statLine = document.querySelector('#statLine')

r.onclick = function(){
    let result = ''
    let player = r.value
    var randomOptions = options[Math.floor(Math.random()*options.length)]
    if (randomOptions === "rock" && player === "scissors"){result = ("Oofff... An L"), l+=1}
    else if (randomOptions === "scissors" && player === "paper"){result = ( "Oofff... An L"), l+=1}
    else if (randomOptions === "paper" && player === "rock"){result = ( "Oofff... An L"), l+=1}
    else if (randomOptions === "rock" && player === "paper"){result = ( "A Dubbie!"), w+=1}
    else if (randomOptions === "paper" && player === "scissors"){result = ( "A Dubbie!"), w+=1}
    else if (randomOptions === "scissors" && player === "rock"){result = ( "A Dubbie!"), w+=1}
    else if (randomOptions === player ){result = ( "A Tie!"), d+=1};
    stats = ("W - "+ w + "L - "+ l + "D - "+ d)
    statLine.innerHTML= `You chose ${player} and the computer chose ... ${randomOptions} which means ${result} and your record is ${stats}`

}
p.onclick = function(){
    let result = ''
    let player = p.value
    var randomOptions = options[Math.floor(Math.random()*options.length)]
    if (randomOptions === "rock" && player === "scissors"){result = ("Oofff... An L"), l+=1}
    else if (randomOptions === "scissors" && player === "paper"){result = ( "Oofff... An L"), l+=1}
    else if (randomOptions === "paper" && player === "rock"){result = ( "Oofff... An L"), l+=1}
    else if (randomOptions === "rock" && player === "paper"){result = ( "A Dubbie!"), w+=1}
    else if (randomOptions === "paper" && player === "scissors"){result = ( "A Dubbie!"), w+=1}
    else if (randomOptions === "scissors" && player === "rock"){result = ( "A Dubbie!"), w+=1}
    else if (randomOptions === player ){result = ( "A Tie!"), d+=1};
    stats = ("W - "+ w + "L - "+ l + "D - "+ d)
    statLine.innerHTML= `You chose ${player} and the computer chose ... ${randomOptions} which means ${result} and your record is ${stats}`

}
s.onclick = function(){
    let result = ''
    let player = s.value
    var randomOptions = options[Math.floor(Math.random()*options.length)]
    if (randomOptions === "rock" && player === "scissors"){result = ("Oofff... An L"), l+=1}
    else if (randomOptions === "scissors" && player === "paper"){result = ("Oofff... An L"), l+=1}
    else if (randomOptions === "paper" && player === "rock"){result = ("Oofff... An L"), l+=1}
    else if (randomOptions === "rock" && player === "paper"){result = ("A Dubbie!"), w+=1}
    else if (randomOptions === "paper" && player === "scissors"){result = ("A Dubbie!"), w+=1}
    else if (randomOptions === "scissors" && player === "rock"){result = ("A Dubbie!"), w+=1}
    else if (randomOptions === player ){result = ("A Tie!"), d+=1}
    stats = ("W - "+ w + "L - "+ l + "D - "+ d)
    statLine.innerHTML= `You chose ${player} and the computer chose ... ${randomOptions} which means ${result} and your record is ${stats}`
}
