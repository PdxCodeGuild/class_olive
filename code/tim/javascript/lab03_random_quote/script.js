let counter = 1
let page = 1
let filter = ''
let btnRandom = document.querySelector('#btn_random')
let btnList = document.querySelector('#btn_list')
let btnPrev = document.querySelector('#btn_prev')
let btnNext = document.querySelector('#btn_next')
let listFilter = document.querySelector('#list_filter')
let btnFilter = document.querySelector('#btn_filter')
let randomBody = document.querySelector('#random_body')
let listBody = document.querySelector('#list_body')

// ######### EVENTS #########
btnRandom.addEventListener('click', function() {
    getRandom()
})

btnList.addEventListener('click', function() {
    getList()
})

btnNext.addEventListener('click', function() {
    nextPage()
})

btnPrev.addEventListener('click', function() {
    prevPage()
})

btnFilter.addEventListener('click', function() {
    console.log(listFilter.value)
    let filter = listFilter.value
    getListFilter(filter)
})

// ######### Random Quote #########
function getRandom(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api/qotd',
    })
    .then((response) => {
        let data = response.data.quote
        // console.log(response.data)
        // console.log(data)
        randomBody.innerHTML = `<h1>Random QOTD</h1>
        "${data.body}"<br> - ${data.author}`
    })
}

// ######### List of Quotes #########
function getList(){
    listBody.innerHTML = ''
    counter = 1
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        params: {'page': page},
        headers: {Authorization: 'Token token="eeed22c50bd575458336e81a152359a6"'}
    })
    .then((response) => {
        console.log('page: ' + response.data.page)
        console.log(response.data)
        response.data.quotes.forEach(quote => {
            document.querySelector('#quote_list').style.display = "block"
            listBody.innerHTML += `<p>${counter}) "${quote.body}"<br>  - ${quote.author}</p>`
            counter++
        })
    })
}

// ######### Filter #########
function getListFilter(filter){
    listBody.innerHTML = ''
    counter = 1
    
    if (filter === ''){
        params = {'page': page,}
    }
    else {
        params = {
            'page': page,
            'filter': filter,
        }
    }
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        params: params,
        headers: {Authorization: 'Token token="eeed22c50bd575458336e81a152359a6"'}
    })
    .then((response) => {
        console.log('page: ' + response.data.page)
        response.data.quotes.forEach(quote => {
            document.querySelector('#quote_list').style.display = "block"
            listBody.innerHTML += `<p>${counter}) "${quote.body}"<br>  - ${quote.author}</p>`
            counter++
        })
    })
}

// Next- put selections on left, full frame on right.  make next/prev buttons work with filter.