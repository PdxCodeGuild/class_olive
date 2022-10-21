// ----------------------------------------Step 1-----------------------------------------
let inputCard = document.querySelector('#inputCard')
let buttonSubmit = document.querySelector('#buttonSubmit')

buttonSubmit.onclick = function(){
    let originalArray = []
    for (i of inputCard.value){
        originalArray.push(i)}
    output1.innerHTML = `<p>1) Original Array: [${originalArray}]</p>`
    console.log('1) Original Array: [' + originalArray + ']' + '\nLength:' + originalArray.length)

// ----------------------------------------Step 2-----------------------------------------
    let checkDigit = originalArray.pop(-1)
    output2.innerHTML = `<p>2) Check Digit: ${checkDigit}</p>
    <p id="UpdatedArray">Updated Array: [${originalArray}]</p>`  // Fix this with CSS later
    console.log('2) Check Digit: ' + checkDigit)

// ----------------------------------------Step 3-----------------------------------------
    let reverseArray = originalArray.reverse()
    output3.innerHTML = `<p>3) Reversed Array: [${reverseArray}]</p>`
    console.log('3) Reversed Array: [' + reverseArray + ']' + '\nLength:' + reverseArray.length)

// ----------------------------------------Step 4-----------------------------------------    
    for (let i = 0; i < reverseArray.length; i++){
        // console.log(reverseArray[i])
        if (i % 2 === 0){
            // console.log('even')
            reverseArray[i] = reverseArray[i] * 2}
        else {
            reverseArray[i] = reverseArray[i] * 1}}
    console.log('4) Doubled Array: [' + reverseArray + ']' + '\nLength:' + reverseArray.length)
    output4.innerHTML = `<p>4) Doubled Array: [${reverseArray}]</p>`
    
// ----------------------------------------Step 5-----------------------------------------
    for (let i = 0; i < reverseArray.length; i++){
        if (reverseArray[i] > 9){
            // console.log(reverseArray[i])
            reverseArray[i] = reverseArray[i] - 9}
        else {
            reverseArray[i] = reverseArray[i] * 1}}
    console.log('5) Minus 9: [' + reverseArray + ']' + '\nLength:' + reverseArray.length)    
    output5.innerHTML = `<p>5) Minus 9: [${reverseArray}]</p>`

// ----------------------------------------Step 6-----------------------------------------
    let sum = 0
    for (listSum of reverseArray){
        sum += listSum
    }
    // console.log(sum)
    console.log('6) Sum: ' + sum)
    output6.innerHTML = `<p>6) Sum: ${sum}</p>`
    
// ----------------------------------------Step 7-----------------------------------------
    let checkDigitSum = String(sum).slice(-1)
    // console.log(checkDigitSum)
    if (checkDigitSum === checkDigit){
        console.log('7) Check digits match')
        output7.innerHTML = `<p>7) Check Digits match.  Card number is valid.</p>`}
    else{
        console.log('7) Check digits do not match')
        output7.innerHTML = `<p>7) Check Digits do not match.  Card number is not valid.</p>`}
}