let inpDistance = document.querySelector('#inpDistance')
let startUnits = document.querySelector('#startUnits')
let endUnits = document.querySelector('#endUnits')
let btnSubmit = document.querySelector('#btnSubmit')

let convert = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
    'yards': 0.9144,
    'inches': 0.0254,
}
// console.table(convert)

btnSubmit.onclick = function(){
    let selectedUnit = startUnits.value
    let outputUnit = endUnits.value
    let convToMeters =  inpDistance.value * convert[selectedUnit]
    let convFromMeters = convToMeters / convert[outputUnit]

    console.log('1) ' + selectedUnit + ': ' + inpDistance.value + ' ->')
    console.log('2) meters: ' + convToMeters + ' ->')
    console.log('3) ' + outputUnit + ': ' + convFromMeters)
    wrap_output.innerHTML = `<br><p>${inpDistance.value} ${selectedUnit} is ${convFromMeters} ${outputUnit}.</p>`
}

