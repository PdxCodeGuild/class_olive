let display = document.querySelector("#display")
let search = document.querySelector("#search")
let quote = document.querySelector("#quote")
let author = document.querySelector("#author")
let filters = document.querySelector("#filters")
let next = document.querySelector("#next")
let page = document.querySelector("#page")
function getDaily(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api/qotd',
    }).then((response) => {
        let qotd = response.data.quote.body
        let quoteAuthor = response.data.quote.author
        quote.innerHTML = qotd
        author.innerHTML = quoteAuthor
        return response
    })
}

getDaily()

function pageNumber(){
    next.value +=1
    searchQuotes()
}

function searchQuotes(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        headers: {Authorization: 'Token token="0d7ed4928ec5ceab5a364c0d3ec85c67"'},
        parameters: {
        page:next.value,
        filter: filters.value
    }
    }).then((response) => {
        let data=''
        let counter=1
        for (let i = 0; i<25; i++){
            data += " - "+response.data.quotes[i].body+"<button>♥</button><br>"
            counter +=1
        }
        display.innerHTML = `${data}`
        return response

    })
}
