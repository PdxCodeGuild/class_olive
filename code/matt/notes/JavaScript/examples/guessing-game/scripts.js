let cardsContainer = document.querySelector("#cards-container")

const cards = [
    {
        'src': 'Chest.png',
        'id': 1
    },
    {
        'src': 'Chest.png',
        'id': 1
    },
    {
        'src': 'Skull.png',
        'id': 2
    },
    {
        'src': 'Skull.png',
        'id': 2
    }
]


const shuffledCards = cards.sort((a, b) => 0.5 - Math.random());
console.log(cards)

for (let i = 0; i < cards.length; i++)
{
    console.log('test')
    let content = `<div class="card"><img src="images/${cards[i].src}"></img></div>`
    let text = document.createElement("div");
    text.innerHTML = content
    document.querySelector('#cards-container').appendChild(text)
}


let cardsNodeArray = document.getElementsByClassName('card')


document.querySelectorAll('.card').forEach(card => {
    // console.log(card)
    card.addEventListener('click', () => {
        card.src = 'images/Coin.png'
        console.log(card.src)
    })
});