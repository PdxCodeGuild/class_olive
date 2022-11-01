// Setting innerText and innerHTML

// You can set the text between a open and close tag (<div>this</div>) using innerText and innerHTML.
// As you might guess, innerText is for text, innerHTML is for a string containing HTML.


let div1 = document.querySelector('#div1')
console.log(div1)
div1.innerHTML = 'Hello world!'

let div2 = document.querySelector('#div2')
div2.innerHTML = '<p><b>Hello World!</b></p>'

//This would renders the following (this code will not run in .js file):

// <div id="div1">Hello World!</div>
// <div id="div2"><p><b>Hello World!</b></p></div>

// Editing Style ------------------------------------------------------------------------------------------


let demo_div = document.querySelector('#demo_div')
demo_div.innerHTML = "Hello World!"
demo_div.style.fontSize = '24px'
demo_div.classList.add("thisClassExists")