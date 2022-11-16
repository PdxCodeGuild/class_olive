const app = Vue.createApp({
    data(){
        return{
            quizList: [],
            quizAmount: 5,
            quizCategory: null,
            quizDifficulty: null,
            currentQuestion: {},
            currentQuestionIndex: -1,
            originalAnswers: [],
            randomAnswers: [],
            totalScore: 0,
            gameStatus: 'chooseCat',
            resultImage: { backgroundImage: "url()"},
        }
    },
    methods: {
        setCategory(buttonCategory){
            this.quizCategory = buttonCategory
            this.gameStatus = 'chooseDiff'
        },
        
        setDifficulty(buttonDifficulty){
            this.quizDifficulty = buttonDifficulty
            console.log(buttonDifficulty)
            console.log(this.quizDifficulty)
            this.startQuiz()
        },

        startQuiz(){
            axios({
                method: 'get',
                url: 'https://opentdb.com/api.php',
                params: {
                    amount: this.quizAmount,
                    category: this.quizCategory,
                    difficulty: this.quizDifficulty,
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
        },

        resetQuiz(){
            this.quizList = []
            this.quizAmount = 10
            this.quizCategory = null
            this.quizDifficulty = null
            this.currentQuestion = {}
            this.currentQuestionIndex = -1
            this.originalAnswers = []
            this.randomAnswers = []
            this.totalScore = 0
            this.resultImage = { backgroundImage: "url()"}
            this.gameStatus = 'chooseCat'
            location.reload()
        },
    },
    mounted(){

    }
})