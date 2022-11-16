const app = Vue.createApp({
    data(){
        return{
        category : '',
        difficulty : '',
        currentQuestion: '',
        Questions: [],
        QuestionsIndex: 0,
        right_answer: '',
        wrong_answers: [],
        score: 0,
        lastAnswer: '',
        attempts: 0,
        result:0,
        finalScore: 0,
        finalAttempts: 0,
        inGame: false,
        pregame: true
        }      

},
    methods: {
        getData(){
            this.inGame=true
            this.pregame=false
            axios({
                method: 'get',
                url: 'https://opentdb.com/api.php',
                params: {
                    amount: 10,
                    category: this.category,
                    difficulty: this.difficulty
                }
            }).then((response) => {
                console.log(response.data)
                this.Questions=response.data.results
                this.currentQuestion= response.data.results[0].question
                this.right_answer= response.data.results[0].correct_answer 
                this.wrong_answers = response.data.results[0].incorrect_answers
                this.decodeAll()
                this.changeQuestionOrder()
                }
                )
          
        },
        changeQuestionOrder(){
            this.wrong_answers.push(this.right_answer)
            for (let i=0; i < this.wrong_answers.length; i++){
   
                var j = Math.floor(Math.random() * (i + 1));
                            
                var temp = this.wrong_answers[i];
                this.wrong_answers[i] = this.wrong_answers[j];
                this.wrong_answers[j] = temp;
            }
            
        },
        GetCorrectAnswer(answer){
            if (answer === this.right_answer){
            this.score++;
            this.finalScore++
        }
            this.lastAnswer=answer
            this.attempts++
            this.finalAttempts++
            this.resetGame()
            this.loadQuestion()
        },

        loadQuestion(){
            if (this.QuestionsIndex === 9){
                this.loadMoreQuestions()
            } 
            else{
                this.QuestionsIndex++
                this.currentQuestion= this.Questions[this.QuestionsIndex].question
                this.wrong_answers=[]
                this.right_answer= this.Questions[this.QuestionsIndex].correct_answer
                this.wrong_answers = this.Questions[this.QuestionsIndex].incorrect_answers
                this.changeQuestionOrder()
            }

            this.decodeAll()
        },

        resetGame(){
            if (this.score === 20){
                this.inGame=false
                this.result= parseInt((this.score / this.attempts) * 100)
                this.score = 0
                this.attempts = 0
                this.currentQuestion = ''
                this.right_answer= ''
                this.wrong_answers= []
                this.lastAnswer= ''
                this.category = ''
                this.difficulty = ''
            }
        },

        
        loadMoreQuestions(){
            this.currentQuestion = ''
            this.wrong_answers= []
            this.QuestionsIndex = 0
            this.getData()
        },

        newGame(){
            this.inGame = true
            this.score = 0
            this.finalScore = 0
            this.finalAttempts = 0
            this.attempts = 0
            this.currentQuestion = ''
            this.right_answer= ''
            this.wrong_answers= []
            this.lastAnswer= ''
            this.category = ''
            this.difficulty = ''
            this.getData()
        },

        decodeAll(){
            this.currentQuestion= this.decode(this.currentQuestion)
            for (let i = 0; i < this.wrong_answers.length; i++) {
                console.log(this.wrong_answers[i]);
                this.wrong_answers[i]= this.decode(this.wrong_answers[i])
              }
        },

        decode(str) {
            let txt = document.createElement("textarea");
            txt.innerHTML = str;
            return txt.value;
        }
    },

        

    setup(){
    }
})

