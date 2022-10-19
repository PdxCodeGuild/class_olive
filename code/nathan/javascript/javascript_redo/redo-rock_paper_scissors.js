const radioButtons = document.querySelectorAll('input[name="selection"]')
const computerOptions = ['rock', 'paper', 'scissors']

const rock = document.querySelector('#rockimg')
const paper = document.querySelector('#paperimg')
const scissors = document.querySelector('#scissorsimg')

const csRock = document.querySelector('#csRock')
const csPaper = document.querySelector('#csPaper')
const csScissors = document.querySelector('#csScissors')

const winner = document.querySelector('#winner')
const theStart = "The winner is....."

const resetGameBtn = document.querySelector('#resetGame')


function decideWinner(theUserSelection, theComputerSelection) {
    const computerWins = `${theStart} the computer.`
    const userWins = `${theStart} you!!!.`

    if (theUserSelection === theComputerSelection) {
        winner.innerHTML = `${theStart} no one. You tied.`
        return
    }
    switch (theUserSelection) {
        case 'rock': {
            if (theComputerSelection === 'paper') {
                winner.innerHTML = computerWins
            }
            else if (theComputerSelection === 'scissors') {
                winner.innerHTML = userWins
            }
            break
        }
        case 'paper': {
            if (theComputerSelection === 'scissors') {
                winner.innerHTML = computerWins
            }
            else if (theComputerSelection === 'rock') {
                winner.innerHTML = userWins
            }
            break
        }
        case 'scissors': {
            if (theComputerSelection === 'rock') {
                winner.innerHTML = computerWins
            }
            else if (theComputerSelection === 'paper') {
                winner.innerHTML = userWins
            }           
        }
        return
    }
    
}

for (let i = 0, len = radioButtons.length; i < len; i++) {
    radioButtons[i].addEventListener('change', function() {     
        let selection = radioButtons[i].value 

        switch (selection) {
            case 'rock': {
                paper.style.visibility = 'hidden'
                scissors.style.visibility = 'hidden'
                break
            }
            case 'paper': {
                rock.style.visibility = 'hidden'
                scissors.style.visibility = 'hidden'
                break
            }
            case 'scissors': {
                rock.style.visibility = 'hidden'
                paper.style.visibility = 'hidden'
            }
        }

        let computerSelection = computerOptions[Math.floor(Math.random() * computerOptions.length)]

        console.log(`The computer selected ${computerSelection}`)

        switch(computerSelection) {
            case 'rock': {
                csRock.style.visibility = 'visible'
                break
            }
            case 'paper': {
                csPaper.style.visibility = 'visible'
                break
            }
            case 'scissors': {
                csScissors.style.visibility = 'visible'
            }
        }

        decideWinner(selection, computerSelection)

    })
}

resetGameBtn.addEventListener('click', function() {
    console.log('hello from reset')
    rock.style.visibility = 'visible'
    paper.style.visibility = 'visible'
    scissors.style.visibility = 'visible'

    csRock.style.visibility = 'hidden'
    csPaper.style.visibility = 'hidden'
    csScissors.style.visibility = 'hidden'

    winner.innerHTML = theStart
})



