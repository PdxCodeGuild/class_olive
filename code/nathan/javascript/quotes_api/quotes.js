api_key = ""

const theQuotes = document.querySelector('#the-quotes')
const nextPageButton = document.querySelector('#next-page-btn')
const backPageButton = document.querySelector('#back-page-btn')
const statusLabel = document.querySelector('#status')
let pageCounter = 1

const myHeaders = {
    "Content-Type": "application/json",
    "Authorization": `Token token="${api_key}"`
}

const url = {'url': 'https://favqs.com/api/quotes'}


async function getQuotes(page){
    try {
    response = await axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        headers: myHeaders,
        params: {'page': page}
    })}catch{
        nextPageButton.style.disabled = true
        statusLabel.style.visibility = 'visible'  
        await new Promise(res => {setTimeout(res, 10000)})
        getQuotes(page)
    }
    stringBuilder = ""
    for(quote of response.data.quotes) {
        stringBuilder += `<div class="quote"><p>${quote.body}</p><div class="authors">-${quote.author}</div><br><br></div>`
    }
    theQuotes.innerHTML = stringBuilder
    statusLabel.style.visibility = 'hidden'
    nextPageButton.style.disabled = false
}

getQuotes(pageCounter)

nextPageButton.addEventListener('click', function(){
    pageCounter++
    getQuotes(pageCounter)
})

