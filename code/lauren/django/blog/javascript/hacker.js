const words = [
    'struct',
    '</br>',
    '</br>',
    '</br>',
    '</br>',
    '</br>',
    '</br>',
    '</br>',
    // '<span class="data">#</span>',
    'group_info',
    '*groups_alloc',
    '(int gridsetsize)',
    'int nblocks',
    'int i;',
    'nblocks =',
    '(gidsetsize)',
    '/ NGROUPS_PER_BLOCK',
    'return NULL;',
    '->',
    'atomic_set',
    '(&group_info)',
    'if',
    'else'
]
let randomIndex = 0
currentWord = ''

let newWord = function() {
    randomIndex = Math.floor(Math.random() * (words.length - 0) + 0)
    currentWord += words[randomIndex]

}
newWord()

let keyCount = 0

document.addEventListener('keypress', (event) => {
    document.querySelector('#content').innerHTML = currentWord
    newWord()
    if(keyCount === 100){
        document.querySelector('#accessContainer').style.display='flex'
    }
    else if (keyCount === 105){
        document.querySelector('#accessContainer').style.display='none'
    }
    else if (keyCount === 200){
        document.querySelector('#deniedContainer').style.display='flex'
    }
    keyCount ++
})



