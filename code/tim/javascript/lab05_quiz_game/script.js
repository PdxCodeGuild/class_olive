const app = Vue.createApp({
    data(){
        return{
            questionsList: '',
        }
    },
    methods: {
        getQuiz(){
            
            axios({
                method: 'get',
                url: 'https://opentdb.com/api.php',
                params: {
                    amount: 10,
                    category: 11,
                    difficulty: 'easy',
                    type: 'multiple',
                }
            }).then((response) => {
                // console.log(response)
                questionsList = response.data.results
                // console.log(questionsList)
                
                for(let i = 0; i < questionsList.length; i++){
                    // console.log(`${this.questionsList}`)
                    // console.log('hi')
                    this.responseQ = questionsList[i].question
                    // console.log(questionsList[i].question)
                    console.table(this.responseQ)
                    }
                    
                return
            })
        }
    },
    setup(){
        // console.log('Hello World')
        // axios({
        //     method: 'get',
        //     url: 'https://opentdb.com/api.php',
        //     params: {
        //         amount: 10,
        //         category: 11,
        //         difficulty: 'easy',
        //         type: 'multiple',
        //     }
        // }).then((response) => {
        //     questionsList = response.data.results
        //     // console.log(questionsList[0].question)
            
        //     for(let i = 0; i < this.questionsList.length; i++){
        //         // console.log(this.questionsList[i].question)
        //         this.responseQ = this.questionsList[i].question
        //         // console.log(this.responseQ)
        //         }
                
        //     return
        // })
    }
})


// function getData(){
//     axios({
//         method: 'get',
//         url: 'https://opentdb.com/api.php',
//         params: {
//             amount: 10,
//             category: 11,
//             difficulty: 'easy',
//             type: 'multiple',
//         }
//     }).then((response) => {
//         let data = response.data.results[0]
//         console.log(response.data.results[0])
//         // console.table(response.data.results[0])
//         // testData = data.difficulty

//         question.innerHTML = data.question
//         answer1.innerHTML = data.incorrect_answers[0]
//         answer2.innerHTML = data.incorrect_answers[1]
//         answer3.innerHTML = data.incorrect_answers[2]
//         answer4.innerHTML = data.correct_answer

//         return response
//     })
// }

// getData()