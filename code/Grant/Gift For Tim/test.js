





let main = document.querySelector('.main')
let uparrow = document.querySelector('.uparrow')
let downarrow = document.querySelector('.downarrow')
let face1 = document.querySelector('.face1')
let face2 = document.querySelector('.face2')
let face3 = document.querySelector('.face3')
let face4 = document.querySelector('.face4')
let leftb = document.querySelector('.leftb')
let rightb = document.querySelector('.rightb')

document.addEventListener('keydown',function(e) {
    
    if(e.key == 'ArrowUp'){
        // console.log('pressed', 'key:' + e.key, 'keyCode:' + e.keyCode);
        uparrow.classList.add('opacity-on');
        console.log('up')
        
    } else if(e.key == 'ArrowDown'){
        // console.log('pressed', 'key:' + e.key, 'keyCode:' + e.keyCode);
        downarrow.classList.add('opacity-on');
        console.log('down')
    } else{
        var facelist = [face1, face2, face3, face4, leftb, rightb]
        // console.log(face1)

        let randomface = facelist[Math.floor(Math.random() * facelist.length)];
        // console.log('any:', facelist[Math.floor(Math.random() * facelist.length)])

        randomface.classList.add('opacity-on')
        
        // console.log('pressed', 'key:' + e.key, 'keyCode:' + e.keyCode);
        
        console.log('anything else')
     }document.addEventListener('keyup',function(e) {
        uparrow.classList.remove('opacity-on');
        downarrow.classList.remove('opacity-on');
        face1.classList.remove('opacity-on');
        face2.classList.remove('opacity-on');
        face3.classList.remove('opacity-on');
        face4.classList.remove('opacity-on');
        leftb.classList.remove('opacity-on')
        rightb.classList.remove('opacity-on')
        
    }
    )
})

var oldScrollY = window.scrollY;

var directionText = document.getElementById('direction');

// window.onscroll = function(e) {
//     if(oldScrollY < window.scrollY){
//         uparrow.classList.remove('opacity-on');
//         downarrow.classList.add('opacity-on');
//         // console.log(downarrow);
//         console.log('down');
//         // console.log(e) 
//     } else{
//         downarrow.classList.remove('opacity-on');
//         uparrow.classList.add('opacity-on');
//         console.log('up');
//     // }else {

//     // }
//     // window.onscroll = function(e) {

//     // }
// }}
