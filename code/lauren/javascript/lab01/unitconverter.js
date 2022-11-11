let distance = document.querySelector('#distance')
let btn = document.querySelector('#btn')
let unit = document.querySelector('#unit')
let unit2 = document.querySelector('#unit2')
btn.onclick = function() {

    let distanceValue = distance.value
    let unitValue = unit.value
    let unitValue2 = unit2.value
    let meters = distance.value * convert[unitValue]
    let result = (meters / convert[unitValue2])
    resultText.innerHTML = result
    
}

let convert = {
  "km": 1000,
  "feet": 0.3048,
  "mile": 1609.34,
  "meter": 1,
  "yard": 0.9144,
  "inch": 0.0254
};


