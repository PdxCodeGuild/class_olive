const app = Vue.createApp({
    data(){
        return{
            questionsList: '',
            amount: 3,
            currentQuestion: 1,
        }
    },
    methods: {
        getQuiz(){
            
            axios({
                method: 'get',
                url: 'https://opentdb.com/api.php',
                params: {
                    amount: this.amount,
                    category: 11,
                    difficulty: 'easy',
                    type: 'multiple',
                }
            }).then((response) => {
                console.log(response.data.results)
                this.questionsList = response.data.results
                // console.log(this.questionsList[0].category)
                
                for (let i = 0; i < this.questionsList.length; i++){
                    // console.log(`${this.questionsList}`)
                    // console.log(this.difficulty)
                    // console.log('hi')
                    if (this.currentQuestion < this.amount)
                    {
                        this.responseQ = this.questionsList[i].question
                        this.correctAnswer = this.questionsList[i].correct_answer
                        console.log(this.amount)
                        break
                        // return
                    }
                }
            })
        }
    },
    mounted(){
        this.getQuiz()

    },
    setup(){
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
        //     this.questionsList = response.data.results
        //     console.log(this.questionsList)
            
        //     for (let i = 0; i < this.questionsList.length; i++){
        //         // console.log(`${this.questionsList}`)
        //         // console.log(this.difficulty)
        //         // console.log('hi')
        //         this.responseQ = this.questionsList[i].question
        //         // this.correctA
                
        //     }
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