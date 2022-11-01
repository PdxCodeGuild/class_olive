let question = document.querySelector('#question')

let answer1 = document.querySelector('#answer1')
let answer2 = document.querySelector('#answer2')
let answer3 = document.querySelector('#answer3')
let answer4 = document.querySelector('#answer4')


function getData(){
    axios({
        method: 'get',
        url: 'https://opentdb.com/api.php',
        params: {
            amount: 10,
            category: 18,
            difficulty: 'easy'
        }
    }).then((response) => {
        let data = response.data.results[0]
        console.log(response.data.results[0])
        testData = data.difficulty

        question.innerHTML = data.question
        answer1.innerHTML = data.incorrect_answers[0]
        answer2.innerHTML = data.incorrect_answers[1]
        answer3.innerHTML = data.incorrect_answers[2]
        answer4.innerHTML = data.correct_answer
        return response
    })
}

getData()
