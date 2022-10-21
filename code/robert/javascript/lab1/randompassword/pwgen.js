let char_len = document.querySelector('#charLen');
let clicked = document.querySelector('#generated');
var charToPick = "01234546789qwaszxerdfcvtyghbnuijkmoplQWASZXERDFCVTYGHBNUIJKMOPL!@#$%^&*()";

genPW.onclick= function(){
    let password = '';
    let pw_len = char_len.value;
    const charToPickLen = charToPick.length;
    for (let i=0; i<pw_len; i++){
        password += charToPick[Math.floor(Math.random()*charToPickLen)]}
    clicked.innerHTML= `Your password is ${password}`
}

