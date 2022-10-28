let people = [
    {
        name: 'Bob',
        age: 45,
        location: 'Oregon',
        id: 1
    },
    {
        name: 'Sarah',
        age: 33,
        location: 'Washington',
        id: 2
    },
    {
        name: 'Doug',
        age: 13,
        location: 'Florida',
        id: 3
    },
    {
        name: 'Jill',
        age: 93,
        location: 'Texas',
        id: 4
    }
]

let container = document.querySelector('#container')
let buildString = ''

function addToDom(){
    people.forEach(person => {
        buildString += `<button onclick="removeItem(${person.id})">${person.name}</button> `
        container.innerHTML = buildString
    })  
    buildString = ''
    
    // forEach does not trigger if length is 0
    if (people.length < 1){
        container.innerHTML = ''
    }
}

function removeItem(id){    
    for (let i = 0; i < people.length; i++)
    {
        if (people[i].id === id){
            people.splice(i, 1) // splice removes from array. first argument is index, second is how many (moving up by index positions)
        }
    }
    addToDom()
}


addToDom()