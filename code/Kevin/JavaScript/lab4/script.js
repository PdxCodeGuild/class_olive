console.log('Hello World!')

let quoteBody = document.querySelector('#quote-body')
let quoteAuthor = document.querySelector('#quote-author')
let userInput = document.querySelector('#user-input')
let quoteDiv = document.querySelector('#quote-div')

let pageCounter = 1


function getData(){
    axios({
            method: 'get',
            url: 'https://favqs.com/api/qotd',
            
        }
    ).then((response) =>{

            console.log(response.data.quote.body, response.data.quote.author)
            quoteBody.innerHTML = response.data.quote.body
            quoteAuthor.innerHTML = '-' + response.data.quote.author
        }
    )
}

getData()

function searchQuotes(){
    console.log(userInput.value)
    axios({
            method: 'get',
            url: 'https://favqs.com/api/quotes/',
            headers: {
                Authorization: 'Token token="76f22d5315672c92f97078a41f365cef"'
            },
            params: {
                page: pageCounter,
                filter: userInput.value
            }
        }
    ).then((response) =>{
        console.log(response)
        for (i=0;i<25;i++)
        {
            let paragraphBody = document.createElement('p')
            let paragraphAuthor = document.createElement('p')
            let br = document.createElement('br')
            paragraphBody.textContent = response.data.quotes[i].body
            quoteDiv.appendChild(paragraphBody)
            paragraphAuthor.textContent = '-' + response.data.quotes[i].author
            quoteDiv.appendChild(paragraphAuthor)
            quoteDiv.appendChild(br)
        }
    })
}

function pageRight(){
    while (quoteDiv.firstChild)
    {
        quoteDiv.removeChild(quoteDiv.firstChild)
    }
    pageCounter++
    searchQuotes()
}

function pageLeft(){
    if (pageCounter > 1)
    {
        while (quoteDiv.firstChild)
        {
            quoteDiv.removeChild(quoteDiv.firstChild)
        }
        pageCounter -= 1
        searchQuotes()
    }

}