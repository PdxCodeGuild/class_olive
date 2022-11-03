
ones_to_text = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
    0 : 'Zero',
    11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'Fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'Nineteen',
    10 : 'Ten'
}
tens_to_text = {
    2 : 'Twenty',
    3 : 'Thirty',
    4 : 'Fourty',
    5 : 'Fifty',
    6 : 'Sixty',
    7 : 'Seventy',
    8 : 'Eighty',
    9 : 'Ninety'
}

let number_value = document.querySelector('#number_value')

numSubmit.onclick = function(){
    var numbText = number_value.value.toString()
    if (number_value.value<20){
        generated.innerHTML = ones_to_text[number_value.value]
    }
    else {
        generated.innerHTML = tens_to_text[numbText[0]] + ones_to_text[numbText[1]]
    }

}