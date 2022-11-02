let slice = ''
let pressedKey = ''
let currentIndex = 16
let terminalOutput = document.querySelector('#terminal_output')
let warningCount = 0
let warningMsg = document.querySelector('#warning_msg')
let warningBtn = document.querySelector('#warning_btn')
let warningDiv = document.querySelector('#warnings')
let warnings = ['Detected intrusion in power cable!','System has been breached!','First firewall breached!','Second firewall breached!','Third firewall breached!','Fourth firewall breached!','Final firewall breached!']

terminalOutput.innerHTML = hacker_text.slice(0,15)
// console.log(hacker_text.length) //6165

let getRandomInt = function(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}

let clock = setInterval(function() {trayClock();}, 1000);
function trayClock() {
    let newTime = new Date();
    document.getElementById("clock").innerHTML = newTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

document.addEventListener('keypress', (event) => {
    let randomInt = getRandomInt(10,20)
    // console.log(`start: ${currentIndex}`)
    // console.log(`random: ${randomInt}`)
    updatedIndex = currentIndex + randomInt
    // console.log(`updated: ${updatedIndex}`)
    slice += hacker_text.slice(currentIndex, updatedIndex)
    currentIndex = updatedIndex
    // console.log(`end: ${currentIndex}`)
    terminalOutput.innerHTML = `<div id="terminalOutputText">${hacker_text.slice(0,15)} ${slice}</div>`
    warningPopups()
})

let warningPopups = function() {
    let startmin = 880
    let startmax = 910
    if (currentIndex > startmin && currentIndex < startmax){
        console.log(currentIndex, startmin, startmax, warningCount)
        // console.log('!!!!! ' + warnings[warningCount])
        warningDiv.style.display = 'block'
        warningMsg.innerHTML = warnings[warningCount]
        warningCount++
        startmin += 880 
        startmax += 880
        console.log(currentIndex, startmin, startmax, warningCount)
    }
}