console.log('Hello World!')

let thingString = ''
let counter = 0

document.getElementById('div1').style.caretColor = 'transparent'

document.querySelector('#div1').innerHTML = 'run "strongbad\'s_email"'
document.addEventListener('keypress', (event) => 
{
    event.preventDefault()
    if (counter === 0)
    {
        document.querySelector('#div1').innerHTML = email
    }
    else if (counter === 1)
    {
        document.getElementById('div1').style.caretColor = 'auto'
        document.querySelector('#div1').innerHTML = ''
    }
    else
    {
        
        document.getElementById('div1').style.caretColor = 'transparent'
        
        thingString += response.charAt(counter -2)
        document.querySelector('#div1').innerHTML = thingString
    }
    counter++
    
    
})

let email = `Dear Strong Bad,
Do you take your wrestling mask and boxing
gloves off before you go to bed?
Sincerely,
Abdi LaRue
San Diego, CA`

let response = `Well, that's a stupid question, Abdi. 
Do you take off your face and hands 
before you go to bed? And if so, are 
you some kind of robot? And if so, 
what kind of powers do you have? 
Do you use them for good, or for 
awesome? Would you like to join 
forces? I just happen to be the 
greatest criminal mind of our 
time.
-Strong Bad`

