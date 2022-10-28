let slice = ''
let pressedKey = ''
let currentIndex = 16
let terminalOutput = document.querySelector('#terminal_output')
let message1 = document.querySelector('#message1')
// let firewall1 = document.querySelector('#firewall1')
// let firewall2 = document.querySelector('#firewall2')
let firewall = document.querySelector('#warning_backtrace')
let firewallMsg = 0
terminalOutput.innerHTML = hacker_text.slice(0,15)

// document.querySelector("terminalOutput").scrollTop = document.querySelector("terminalOutput").scrollHeight

let getRandomInt = function(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}

// let firewallBreach = function(index){
//     if (index >= 20 && index <= 39 && firewallMsg === 0){
//         console.log('firewall 1 - ' + index)
//         firewall.innerHTML += '<ul>firewall 1</ul>'
//         ++firewallMsg
//     } 
//     if (index >= 40 && index <= 59 && firewallMsg === 1){
//         console.log('firewall 2 - ' + index)
//         firewall.innerHTML += '<ul>firewall 2</ul>'
//         ++firewallMsg
// }}

var myVar = setInterval(function() {
    myTimer();
}, 1000);
    
function myTimer() {
    var d = new Date();
    document.getElementById("clock").innerHTML = d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}


document.addEventListener('keypress', (event) => {
    let randomInt = getRandomInt(10,29)
    // console.log(`start: ${currentIndex}`)
    // console.log(`random: ${randomInt}`)
    updatedIndex = currentIndex + randomInt
    // console.log(`updated: ${updatedIndex}`)
    slice += hacker_text.slice(currentIndex, updatedIndex)
    currentIndex = updatedIndex
    // console.log(`end: ${currentIndex}`)
    terminalOutput.innerHTML = `<div id="terminalOutputText">${hacker_text.slice(0,15)} ${slice}</div>`
    // firewallBreach(currentIndex)
    // if (currentIndex >= 55 && currentIndex <= 75 ){
    //     console.log('!!!!!true - ' + currentIndex)
    //     message1.innerHTML = `<ul>ruh roh i see you</ul>`
    // }
})