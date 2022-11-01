
// Turn Text green: something simple you easily could do with just css or though js. 
gsap.to('#green-sock', { color: 'green' })

// Rotate Text color: much less robust and easy to understand than vanilla js or css versions
// -1 is an infinite loop. If it was 4, it would loop 4 times
let tl = gsap.timeline({ repeat: -1})
tl.to('#rotating-text', {color: 'red'})
tl.to('#rotating-text', {color: 'blue'})
tl.to('#rotating-text', {opacity: 0})

let toggleBtn = document.querySelector('#toggle-btn')
let toggle = false


toggleBtn.addEventListener('click', () => {
    if (toggle)
    {
        gsap.to("#app", {background: '#ffd000'})
    }
    else{
        gsap.to("#app", {background: '#87ceeb'})
    }
    toggle = !toggle
})


let balloonBtn = document.querySelector('#balloon-btn')

balloonBtn.addEventListener('click', () => {
    gsap.to('#balloon', {display: 'block'})
    gsap.to('#balloon', {duration: 20, y: '-70vh', x: '70vw'})

    let tl = gsap.timeline({ repeat: 6 })
    tl.to('#balloon', {duration: 1, rotate: '2deg'})
    tl.to('#balloon', {duration: 1, rotate: '-2deg'})
    tl.to('#balloon', {duration: 1, rotate: '-0deg'})
})




gsap.to('#triggers-container', { 
    scrollTrigger : {
        trigger: '#triggers-container',
        start: '-100 center',
        end: 'bottom center',
        toggleAction: 'play none none none',
        // toggleActions events: onEnter, onLeaves, OnEnterBack, OnLeaveBack  (they are in order)
        // options: play, pause, resume, reset, restart, complete, reverse, none
        scrub: 1,  // when scrolling back before event, restores it to previous state.
        // markers:true
    },
    opacity: 1,

})

