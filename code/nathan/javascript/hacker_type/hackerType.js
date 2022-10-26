text = "importScripts('md5.js', 'chars.js')<br>\
<br>\
// Cracking settings<br>\
var workerId<br>\
&emsp;&emsp;, maxPassLength = undefined<br>\
&emsp;&emsp;, passToCrack = undefined<br>\
  <br>\
// Timer variables<br>\
var interval = 100000<br>\
&emsp;&emsp;, count = 0<br>\
&emsp;&emsp;, startTime = +new Date<br>\
  <br>\
function status(msg) {<br>\
    &emsp;&emsp;this.postMessage( {cmd: \"status\", data: msg, id: workerId })<br>\
}<br>\
function log(msg) {<br>\
    &emsp;&emsp;this.postMessage( {cmd: \"log\", data: msg, id: workerId })<br>\
}<br>\
<br>\
function crack(options) {<br>\
    &emsp;&emsp;status(\"Started cracking\")<br>\
  <br>\
  var hop = options.hop<br>\
  &emsp;&emsp;, length = 1<br>\
  &emsp;&emsp;, buf = new ArrayBuffer(maxPassLength)<br>\
  &emsp;&emsp;, bufView = new Uint8Array(buf)<br>\
  &emsp;&emsp;, view = bufView.subarray(maxPassLength - length)<br>\
  &emsp;&emsp;, numBefore, num, pw<br>\
    <br>\
  bufView[maxPassLength - 1] = from + options.start <br>\
  <br>\
  while (true) {<br>\
    &emsp;&emsp;pw = String.fromCharCode.apply(null, view)<br>\
    <br>\
    if (md5(pw) == passToCrack) {<br>\
        &emsp;&emsp;this.postMessage({ cmd: \"foundPassword\", data: pw, id: workerId })<br>\
        &emsp;&emsp;return<br>\
    }<br>\
    <br>\
    numBefore = view[length - 1]<br>\
    num = (view[length - 1] += hop)<br>\
    <br>\
    // Skip over whole \"skip ranges\", like they don't exist<br>\
    if (numBefore < skip1_from && num >= skip1_from) {<br>\
        &emsp;&emsp;view[length - 1] = skip1_to + (num - skip1_from)<br>\
      <br>\
    } else if (numBefore < skip2_from && num >= skip2_from) {<br>\
        &emsp;&emsp;view[length - 1] = skip2_to + (num - skip2_from)<br>\
    }<br>\
    <br>\
    // Check if we need to carry any numbers<br>\
    // Check from right to left<br>\
    for (var i = length - 1; i >= 0; --i) {<br>\
        <br>\
      if (view[i] >= to) {    <br>\
        &emsp;&emsp;// need to carry<br>\
        <br>\
        &emsp;&emsp;view[i] = (view[i] % to) + from<br>\
        <br>\
        if (i == 0) {<br>\
            &emsp;&emsp;// need to add a new \"place\" to the left<br>\
          <br>\
          &emsp;&emsp;length += 1<br>\
          &emsp;&emsp;view = bufView.subarray(maxPassLength - length)<br>\
          &emsp;&emsp;view[0] = from<br>\
          <br>\
          if (length > maxPassLength)<br>\
          &emsp;&emsp;return<br>\
            <br>\
        } else {<br>\
          // need to carry a number to the left \"place\"<br>\
          num = (view[i - 1] += 1)<br>\
          <br>\
          // Skip over whole \"skip ranges\" for everything but<br>\
          // the \"ones place\"<br>\
          if (num == skip1_from) {<br>\
            &emsp;&emsp;num = (view[i - 1] = skip1_to)<br>\
          }<br>\
          if (num == skip2_from) {<br>\
            &emsp;&emsp;num = (view[i - 1] = skip2_to)<br>\
            &emsp;&emsp;}<br>\
            &emsp;&emsp;}<br>\
            &emsp;&emsp;<br>\
            &emsp;}<br>\
    }<br>\
    <br>\
    // Timer stuff<br>\
    count += 1<br>\
    if (count % interval == 0) {<br>\
        &emsp;&emsp;this.postMessage({ cmd: \"setRate\", data: interval / ((new Date - startTime) / 1000), id: workerId })<br>\
        &emsp;&emsp;count = 0<br>\
        &emsp;&emsp;startTime = +new Date<br>\
        &emsp;&emsp;}<br>\
        &emsp;}<br>\
  <br>\
}<br>\
<br>\
this.addEventListener('message', function(e) {<br>\
    <br>\
  switch (e.data.cmd) {<br>\
    &emsp;case \"setWorkerId\":<br>\
    &emsp;&emsp;workerId = e.data.data<br>\
    &emsp;&emsp;break<br>\
      <br>\
      &emsp;case \"setMaxPassLength\":<br>\
    &emsp;&emsp;maxPassLength = e.data.data<br>\
    &emsp;&emsp;break<br>\
      <br>\
      &emsp;case \"setPassToCrack\":<br>\
      &emsp;&emsp;passToCrack = e.data.data<br>\
      break<br>\
      <br>\
      &emsp;case \"performCrack\":<br>\
      &emsp;&emsp;crack(e.data.data)<br>\
      &emsp;&emsp;break<br>\
      <br>\
    default:<br>\
    &emsp;&emsp;this.postMessage({ cmd: \"log\", data: \"Worker doesn't understand command \" + e.data.cmd })<br>\
    &emsp;&emsp;break<br>\
      <br>\
      &emsp;}<br>\
  <br>\
})"

let textArray = text.split(' ')
let shellText = "PS C:\\Users\\Hacker> "
let i = 0
let gifCounter = 0

const textArea = document.querySelector('#textArea')
const body = document.querySelector('#body')
const gif1 = document.querySelector('#gif1')
const gif2 = document.querySelector('#gif2')
const gif3 = document.querySelector('#gif3')
const gif4 = document.querySelector('#gif4')
const gifs = [gif1, gif2, gif3, gif4]

body.addEventListener('keypress', function() {
    if(i >= textArray.length) {
        i = 0
    }
    shellText += textArray[i]
    i++
    textArea.innerHTML = shellText
})

body.addEventListener('keypress', function(e) {
    if(e.key === 'Enter') {
        if(gifCounter >= gifs.length) {
            gifCounter = 0
        }
        gifs[gifCounter].style.visibility = 'visible'
        if(gifCounter === 0) {
            gifs[gifs.length - 1].style.visibility = 'hidden'
        }
        else {  gifs[gifCounter - 1].style.visibility = 'hidden'
        }
        gifCounter++
    }
})

body.addEventListener('keypress', function(e) {
  if(e.key === '?') {
    body.style.backgroundImage = "url(https://media0.giphy.com/media/WoD6JZnwap6s8/giphy.gif?cid=ecf05e47t7b5a273658pubj3rt1yda1eylpzrra75kah3tpl&rid=giphy.gif&ct=g)"
  }
})