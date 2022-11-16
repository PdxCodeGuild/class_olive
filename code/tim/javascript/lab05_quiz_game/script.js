const app = Vue.createApp({
    data(){
        return{
            quizList: [],
            quizAmount: 10,
            quizCategory: null,
            currentQuestion: {},
            currentQuestionIndex: -1,
            originalAnswers: [],
            randomAnswers: [],
            totalScore: 0,
            gameStatus: 'waiting',
            resultImage: { backgroundImage: "url()"},
            playerResult: '',
        }
    },
    methods: {
        setCategory(buttonCategory){
            this.quizCategory = buttonCategory
            this.startQuiz()
        },
        
        startQuiz(){
            axios({
                method: 'get',
                url: 'https://opentdb.com/api.php',
                params: {
                    amount: this.quizAmount,
                    category: this.quizCategory,
                    difficulty: 'easy',
                    type: 'multiple',
                }
            }).then((response) => {
                this.quizList = response.data.results
                this.gameStatus = 'playing'
                this.nextQuestion()

            })
        },

        decode(str) {
            let txt = document.createElement("textarea");
            txt.innerHTML = str;
            return txt.value;
        },

        nextQuestion(){
            if (this.currentQuestionIndex === (this.quizAmount -1)){
                this.gameOver()
            }

            else if (this.currentQuestionIndex <= (this.quizAmount -1)){
                this.resultImage['backgroundImage'] = ""
                this.currentQuestionIndex++
                this.currentQuestion = this.quizList[this.currentQuestionIndex]
                this.originalAnswers = this.currentQuestion.incorrect_answers
                this.originalAnswers.push(this.currentQuestion.correct_answer)
                this.randomAnswers = this.originalAnswers.sort((a, b) => 0.5 - Math.random());
                console.log('Answer - ' + this.currentQuestion.correct_answer)
            }
        },

        checkAnswer(buttonValue){
            if (buttonValue === this.currentQuestion.correct_answer){
                this.resultImage['backgroundImage'] = "url(./correct.png)"
                this.totalScore += (this.currentQuestionIndex + 1) * 100
            }
            else{
                this.resultImage['backgroundImage'] = "url(./incorrect.png)"
                console.log('Wrong.  Answer is ' + this.currentQuestion.correct_answer)
                this.totalScore -= (this.currentQuestionIndex + 1) * 100
            }
            setTimeout(() => {this.nextQuestion(); }, 1000);
        },

        gameOver(){
            this.gameStatus = 'over'
            console.log('game over')
            
            if (this.totalScore > 0){
                console.log(this.totalScore + 'is positive')
                this.playerResult = 'winner'
            }
            else{
                console.log(this.totalScore + 'is negative')
                this.playerResult = 'loser'
            }
        },

        resetQuiz(){
            this.quizList = []
            this.quizAmount = 10
            this.quizCategory = null
            this.currentQuestion = {}
            this.currentQuestionIndex = -1
            this.originalAnswers = []
            this.randomAnswers = []
            this.totalScore = 0
            this.resultImage = { backgroundImage: "url()"}
            this.gameStatus = 'waiting'
            this.playerResult = ''
            location.reload()
        },
    },
    mounted(){

    }
})