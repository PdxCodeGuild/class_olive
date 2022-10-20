let inputCard = document.querySelector('#inputCard')
let buttonSubmit = document.querySelector('#buttonSubmit')

buttonSubmit.onclick = function() {

    // console.log('Original Number:' + inputCard.value)
    
let originalArray = []

for (i of inputCard.value){
    originalArray.push(i)
}

output1.innerHTML = `<p>1) Original Array: [${originalArray}]</p>`
    console.log('1) Original Array: [' + originalArray + ']' + '\nLength:' + originalArray.length)

let checkDigit = originalArray.pop(-1)
    
output2.innerHTML = `<p>2) Check Digit: ${checkDigit}</p>
    <p>&nbsp&nbsp&nbsp&nbspUpdated Array: [${originalArray}]</p>`  // Fix this with CSS later

    console.log('2) Check Digit: ' + checkDigit)

let reverseArray = originalArray.reverse()

output3.innerHTML = `<p>3) Reversed Array: [${reverseArray}]</p>`
    console.log('3) Reversed Array: [' + reverseArray + ']' + '\nLength:' + reverseArray.length)

    
    for (i of reverseArray){
        if (i % 2 == 1){
            i = i * 2
            console.log(i)
        }
        
        if (i > 9 == 1){
            i = i - 9
            console.log(i)
        }
    }
    
    console.log('4) Doubled Array: [' + reverseArray + ']' + '\nLength:' + reverseArray.length)
    
}


// TODO -- make a new empty list, copy indexes one at a time.  if even, double it then -9 if needed, 
// then i++ and copy the odd unchanged, then loop back to even until done.