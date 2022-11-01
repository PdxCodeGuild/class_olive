// Overview
// JavaScript provides many functions to manipulate the DOM. You can find more info on MDN and w3schools.

// Accessing Elements
// You can access the elements of the DOM from JavaScript using several functions.


// function
// document.querySelector(selector)				get an element that matches the given CSS selector
// document.querySelectorAll(selector)			get all elements that match the given CSS selector
// document.getElementById(id)					get an element with the given id
// document.getElementsByTagName(tag)			get all elements of the given tag
// document.getElementsByName(name)				get all elements with the given name


// Example of getting an element by querySelector
// let container = document.querySelector('#container') 

// Example of getting an element by ID
// let container = document.getElementById('container')


let container = document.querySelector('#container') 
console.log(container)
container.style.background = '#87ceeb'
container.style.padding = '1rem'


let title = document.querySelector('#title')
console.log(title)
title.style.color = 'white'
title.style.fontSize = '2rem'


let pTag = document.querySelectorAll('.words')
console.log(pTag) // gives a node list, not a single element
pTag[1].style.color = 'black'
pTag[1].style.fontSize = '1.5rem'
