// gsap.from('#ship', {
//     scrollTrigger : '#ship',
//     start: 'center center',
//     end: 'bottom bottom',
//     scrub: true, 
//     options: 'restart',
//     duration: 3,
//     x: 500  
// })

// scrollTrigger : {
//     trigger: '#triggers-container',
//     start: '-100 center',
//     end: 'bottom center',
//     toggleAction: 'play none none none',
//     // toggleActions events: onEnter, onLeaves, OnEnterBack, OnLeaveBack  (they are in order)
//     // options: play, pause, resume, reset, restart, complete, reverse, none
//     scrub: 1,  // when scrolling back before event, restores it to previous state.
//     // markers:true
// }

let observerShip = new IntersectionObserver(function() {
    let tween = gsap.from('#ship', { duration: 3, x: 500})
    if (tween.isActive()) {
        return
    }
    else {
        tween.play()
    }
}, { root: null });

let observerPlane = new IntersectionObserver(function() {
    let tween = gsap.from('#plane', { duration: 3, x: 1000})
	if (tween.isActive()) {
        return
    }
    else {
        tween.play()
    }
}, { root: null });

let observerPlane2 = new IntersectionObserver(function() {
    let tween = gsap.from('#plane2', { duration: 6, x: 1000})
	if (tween.isActive()) {
        return
    }
    else {
        tween.play()
    }
}, { root: null });

let observerPlane3 = new IntersectionObserver(function() {
    let tween = gsap.from('#plane3', { duration: 3, x: 1000})
	if (tween.isActive()) {
        return
    }
    else {
        tween.play()
    }
}, { root: null });

let observerPlane4 = new IntersectionObserver(function() {
    let tween = gsap.from('#plane4', { duration: 3, x: 1000})
	if (tween.isActive()) {
        return
    }
    else {
        tween.play()
    }
}, { root: null });

let observerPlane5 = new IntersectionObserver(function() {
    let tween = gsap.from('#plane5', { duration: 3, x: 1000})
	if (tween.isActive()) {
        return
    }
    else {
        tween.play()
    }
}, { root: null });


observerShip.observe(document.querySelector("#ship"));
observerPlane.observe(document.querySelector("#plane"));
observerPlane2.observe(document.querySelector("#plane2"));
observerPlane3.observe(document.querySelector("#plane3"));
observerPlane4.observe(document.querySelector("#plane4"));
observerPlane5.observe(document.querySelector("#plane5"));

