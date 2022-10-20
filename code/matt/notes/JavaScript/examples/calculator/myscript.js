let num1 = document.querySelector('#num1')
let num2 = document.querySelector('#num2')

let multOp = document.querySelector('#multOp')
let divOp = document.querySelector('#divOp')
let subOp = document.querySelector('#subOp')
let addOp = document.querySelector('#addOp')

let resultText = document.querySelector('#resultText')

multOp.onclick = function() {
    let result = num1.value * num2.value
    resultText.innerHTML = `${num1.value} * ${num2.value} = ${result}`
}

divOp.onclick = function() {
    let result = num1.value / num2.value
    resultText.innerHTML = `${num1.value} / ${num2.value} = ${result}`
}

subOp.onclick = function() {
    let result = num1.value - num2.value
    resultText.innerHTML = `${num1.value} - ${num2.value} = ${result}`
}

addOp.onclick = function() {
    // console.log(typeof num1.value)
    let result = parseInt(num1.value) + parseInt(num2.value)
    // console.log(typeof result)
    resultText.innerHTML = `${num1.value} + ${num2.value} = ${result}`
}





