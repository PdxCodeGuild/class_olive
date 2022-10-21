const alphabetLower = 'abcdefghijklmnopqrstuvwxyz'.split('')
const alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')
const numbers = '1234567890'.split('')
const symbols = '!@#$%^&*()_-+'.split('')

const alphaNumericChars = [].concat(alphabetLower, alphabetUpper, numbers, symbols)
const generateButton = document.querySelector('#generate')
const resultBox = document.querySelector('#resultBox')

generateButton.addEventListener('click', function() {

    let passwordLength = document.querySelector('#numberChoice').value
    let result = ''

    for (let i=0; i < passwordLength; i++) {
        result += alphaNumericChars[Math.floor(Math.random() * alphaNumericChars.length)]
    }
    resultBox.value = result
})

