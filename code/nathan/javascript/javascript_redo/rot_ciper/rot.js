const encryptText = document.querySelector('#encrypt')
const decryptText = document.querySelector('#decrypt')
const encryptResult = document.querySelector('#encryptResult')
const decryptResult = document.querySelector('#decryptResult')
const history = document.querySelector('#history')
const body = document.querySelector('#body')

const alphabetLower = 'abcdefghijklmnopqrstuvwxyz'.split('')

function encrypt(input) {
    let encryptedText = ''
    for(letter of input.toLowerCase()) {
        let index = alphabetLower.indexOf(letter)
        index += 13
        if (index > 25) {
            index -= 26
        }
        encryptedText += alphabetLower[index]
    }
    return encryptedText
}

function decrypt(input) {
    let decryptedText = ''
    for(letter of input.toLowerCase()) {
        let index = alphabetLower.indexOf(letter)
        index -= 13
        if (index < 0) {
            index += 26
        }
        decryptedText += alphabetLower[index]
    }
    return decryptedText
}

function addHistory(input, output) {
    history.style.visibility = 'visible'
    history.innerHTML += `Input: ${input}&ensp;Output: ${output}&emsp;`
}

encryptText.addEventListener('click', function() {
    decryptText.value = ''
    encryptResult.value = ''
    decryptResult.value = ''
})

decryptText.addEventListener('click', function() {
    encryptText.value = ''
    encryptResult.value = ''
    decryptResult.value = ''
})

body.addEventListener('keypress', function(e) {
    if(e.key === 'Enter') {
        if (encryptText.value === '') {
            decryptResult.value = decrypt(decryptText.value)
            addHistory(decryptText.value, decryptResult.value)
            decryptText.value = ''
            return
        }
        if (decryptText.value === '') {
            encryptResult.value = encrypt(encryptText.value)
            addHistory(encryptText.value, encryptResult.value)
            encryptText.value = ''
            return
        }
    }
})
