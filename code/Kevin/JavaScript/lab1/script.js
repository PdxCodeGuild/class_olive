

function randomSixNumbers()
{
    const randomNumbers = []
    for (i=0; i < 6; i++)
    {
        let randomNumber = Math.floor(Math.random() * 100 );
        randomNumbers[i] = randomNumber
    
    }
    return randomNumbers

}

function pickSix()
{
    const winnings = ['nothing!','$4!','$7!','$100!','$500,000!','$1,000,000!','$25,000,000!!!!!']
    let score = 0
    const winningNumbers = randomSixNumbers()
    const playerNumbers = document.getElementById('userPick6').value.split(',')
    console.log(playerNumbers)
    for (i=0; i < 6 ; i++)
    {
        // console.log(playerNumbers[i], 'player numbers')
        if (winningNumbers[i] == playerNumbers[i])
        {
            score++
        }
    }
    document.getElementById('userPick6').value = ''
    return console.log('you won ' + winnings[score])
}
function pickSixMulti()
{
    const winnings = [0,4,7,100,500000,1000000,25000000]
    let cost = 0
    let earnings = 0
    const winningNumbers = randomSixNumbers()
    console.log(winningNumbers, 'winning numbers')
    for (let i=0; i < document.getElementById('userPick6Multi').value; i++)
    {
        let playerNumbers = randomSixNumbers()
        console.log(playerNumbers, 'player numbers')
        cost += 2
        let score = 0
        for (let x=0; x < 6 ; x++)
        {
            if (winningNumbers[x] == playerNumbers[x])
            {
                score++
            }
        }
        earnings += winnings[score]
    }
    dollarSign = '$'
    if (earnings == 0)
    {
        dollarSign = ''
        earnings = 'nothing'
    }
    document.getElementById('userPick6Multi').value = ''
    return console.log(`You earned ${dollarSign}${earnings}! You owe $${cost}!`)
}


const convertDict = {
    'meters': 1,
    'feet': 0.3048,
    'miles': 1609.34,
    'kilometers': 1000,
    'yards': 0.9144,
    'inches': 0.0254
}

function convertUnits()
{
    let userUnit = ''
    let convertUnit = ''
    let userDistance = document.querySelector('#userDistance').value
    let userRadios = document.getElementsByName('userRadios')
    let convertRadios = document.getElementsByName('convertRadios')
    for (i=0; i < userRadios.length; i++)
    {
        if (userRadios[i].checked == true)
        {
            userUnit = userRadios[i].value
        }
    }
    for (i=0; i < convertRadios.length; i++)
    {
        if (convertRadios[i].checked == true)
        {
            convertUnit = convertRadios[i].value
        }
    }
    let mathTime = userDistance * convertDict[userUnit]
        mathTime = mathTime / convertDict[convertUnit]
    console.log(`${userDistance} ${userUnit} converts to ${mathTime} ${convertUnit}`)
}


const cardDict = {
    'A11':11,
    'A1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10
}

function blackjack()
{
    let card1 = document.querySelector('#card1').value
    let card2 = document.querySelector('#card2').value
    let card3 = document.querySelector('#card3').value

    let handTotal = cardDict[card1] + cardDict[card2] + cardDict[card3]
    
    if (handTotal < 17)
    {
        console.log('Hit')
    }
    else if (handTotal < 21)
    {
        console.log('Stay')
    }
    else if (handTotal == 21)
    {
        console.log('Blackjack!')
    }
    else if (handTotal > 21)
    {
        console.log('Bust')
    }

}

