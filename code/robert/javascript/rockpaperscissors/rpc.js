var options = [
    "r",
    "p",
    "s"
];

var randomOptions = options[Math.floor(Math.random()*options.length)];
//console.log(randomOptions)//test

let playAgain = true
let w = 0
let l = 0
let d = 0

function rpc(randomOptions){
    const clicks = document.getElementsByTagName('button');
    const clicky = clicked => {
    console.log("You've Selected "+ clicked.target.value)
    

    for (let click of clicks){
        click.addEventListener("click",clicky)
    }
    
    let player=clicked.target.value
    console.log(player)

    if (randomOptions === "r" && player === "s"){console.log("Oofff... An L"), l+=1}
    else if (randomOptions === "s" && player === "p"){console.log( "Oofff... An L"), l+=1}
    else if (randomOptions === "p" && player === "r"){console.log( "Oofff... An L"), l+=1}
    else if (randomOptions === "r" && player === "p"){console.log( "A Dubbie!"), w+=1}
    else if (randomOptions === "P" && player === "s"){console.log( "A Dubbie!"), w+=1}
    else if (randomOptions === "s" && player === "r"){console.log( "A Dubbie!"), w+=1}
    else if (randomOptions === player ){console.log( "A Tie!"), d+=1}
    console.log("W - "+ w + " L - "+ l + " D - "+ d)
}}
