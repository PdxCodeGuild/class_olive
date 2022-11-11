let todoObject = [
    {
        name: 'Eat',
        completed: false,
        id: 1
    },
    {
        name: 'Sleep',
        completed: true,
        id: 2
    }   
]
let submit = document.querySelector('#submit-btn')
let todoSection = document.querySelector('#todos-section')
let completedSection = document.querySelector('#completed-section')
let counter = 2
submit.onclick = function() {
    let userInput = document.querySelector('#userInput').value
    counter++
    let newItem = 
    { 
        name: userInput,
        completed: false,
        id: counter
    }
    todoObject.push(newItem)
    addToDom()
}
function addToDom(){
    console.log('adToDom triggered')
    let todoSection = document.querySelector('#todos-section')
    let todoString = ''
    let doneString = ''
    todoObject.forEach(task => {
        console.log('inside for loop')
        if (task.completed === false)
        {
            todoString += `<p>${task.name}</p> <button onclick="completeTodo(${task.id})">complete</button> <button onclick="deleteTodo(${task.id})">remove</button>`
        }
        else if (task.completed === true)
        {
            doneString += `<p>${task.name}</p> <button onclick="completeTodo(${task.id})">incomplete</button> <button onclick="deleteTodo(${task.id})">remove</button>`
        }

    }) 
    
    todoSection.innerHTML = todoString
    completedSection.innerHTML = doneString
}
function completeTodo(id) {
    todoObject.forEach(task =>
        {
            if (task.id === id)
            {
            task.completed = !task.completed
            }
            console.log(task.completed)
            addToDom()
            
        } 
)}
function deleteTodo(id) {
    todoObject.forEach(task =>
        {
            if (task.id === id)
            {
                todoObject.splice(todoObject.indexOf(task),1)
                console.log(todoObject)
            }
            
            addToDom()
        } 
    )}
// initializes the first todos 
addToDom()