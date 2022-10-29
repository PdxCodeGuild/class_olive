const todoObject = [
    {
        name: 'Eat',
        completed: false,
        id: 0
    },
    {
        name: 'Sleep',
        completed: false,
        id: 1
    }   
]
let submit = document.querySelector('#submit-btn')
let todoSection = document.querySelector('#todos-section')
let completedSection = document.querySelector('#completed-section')
let inputTodo = document.querySelector('#input-todo')
let counter = todoObject.length
submit.onclick = function() {
    let newObject = { name: inputTodo.value, completed: false, id: (counter++)}
    todoObject.push(newObject)
    addToDom()
}
function addToDom(){
    todoSection.innerHTML = ""
    completedSection.innerHTML = ""
    todoObject.forEach(task => {
        if(!task.completed) 
        {
            todoSection.innerHTML += `<p>${task.name}</p> <button onclick="completeTodo(${task.id})">Complete</button> <button onclick="deleteTodo(${task.id})">Delete</button>`
        }
        else
        {
            completedSection.innerHTML += `<p>${task.name}</p> <button onclick="completeTodo(${task.id})">Uncomplete</button> <button onclick="deleteTodo(${task.id})">Delete</button>`
        }
        }
    )
        if(todoObject.length === 0)
        {
            todoSection.innerHTML = ""
            completedSection.innerHTML = ""
        }
        // console.table(todoObject)
}
function completeTodo(id) {
    for(let i = 0; i < todoObject.length; i++)
    {
        if(todoObject[i].id === id)
        {
            todoObject[i].completed =  !todoObject[i].completed
        }
    }    
    addToDom()
}

function deleteTodo(id) {
    for(let i = 0; i < todoObject.length; i++)
    {
        if(todoObject[i].id === id)
        {
            todoObject.splice(i, 1)
        }
    }   
    // console.table(todoObject)
    addToDom()
}
// initializes the first todos 
addToDom()