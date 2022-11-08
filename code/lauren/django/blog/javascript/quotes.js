let quote = document.querySelector('#quote')
let author = document.querySelector('#author')
let userInput = document.querySelector('#term')
let button = document.querySelector('#btn')
let page = 1
let quotesArray = []


function getQuote(){
    console.log(userInput.value)
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        
        headers: {
            Authorization: 'Token token="46c94880c7c120b0b0d806c44fdd9b8e"'
        },
        params: {
            page: page,
            filter: userInput.value

        }
      
    }).then((response) => {
    quote.innerHTML = ''
    // author.innerHTML = response.data.quotes[0].author
    quotesArray = response.data.quotes
    for ( let i = 0; i < quotesArray.length; i++){
        quote.innerHTML += `<p>${quotesArray[i].body}</p>`
    }
    
    console.log(response.data.quotes)
    
        
    })
}

function nextPage() {
    page++
    getQuote()
}

// button.onclick = function() {
//     getQuote()
// }


