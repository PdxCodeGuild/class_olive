// Template Literals ------------------------------------------------------------------

let taco_count = 9

// the long hard way
// console.log('You had ' + taco_count + ' tacos at the wedding and you feel ashamed') 

// the ideal way. Basically a python f string
console.log(`You had ${taco_count} tacos at the wedding and you feel ashamed`)


function getFullName(title, firstName, lastName, degree){
    return `${title} ${firstName} ${lastName} ${degree}`
}

// returns 'Rear Admiral Grace Hopper, PhD'
console.log(getFullName('Admiral', 'Grace', 'Hopper', 'PHD'))

// String Methods --------------------------------------------------------------------

//          01234
let text = 'hello'
console.log(text[0]) // h
console.log(text[1]) // e
console.log(text.length) // 5
console.log(text.charAt(1)) // e


// Concatenation: s1+s2, s1.concat(s2, s3, ...) ---------------------------------------

let s = 'hello' + ' ' + 'world'
console.log(s)


// Concatenation is loose with type casting. JS will typecast this int to a string

let m = 'My age is ' + 30
console.log(m)  // My age is 30

// Index of a Substring --------------------------------------------------------------------

let n = 'hello world, hello moon'
console.log(n.indexOf('w')) // 6
console.log(n.indexOf('hello')) // 0
console.log(n.indexOf('llo')) // 2
console.log(n.lastIndexOf('hello')) // 13

// Includes: s1.includes(s2) -----------------------------------------------------------------

let o = 'hello world'
console.log(o.includes('hello')) // true
console.log(o.includes('goodbye')) // false

// Changing Case: s.toUpperCase(), s.toLowerCase() --------------------------------------------

let p = 'Hello World!'
console.log(p.toUpperCase()) // HELLO WORLD!
console.log(p.toLowerCase()) // hello world!

// Split: s.split(delimiter) --------------------------------------------------------------------

let fruits = 'apples bananas plums'
fruits = fruits.split(' ') // split on space
console.log(fruits) // ['apples', 'bananas', 'plums']

let fruits_2 = ['apples', 'bananas', 'plums']
fruits_2 = fruits_2.join(', ') // join with a comma-space
console.log(fruits_2)  // apples, bananas, plums



// let names = ['bob', 'tim']

// names.push('greg')
// console.log(names)