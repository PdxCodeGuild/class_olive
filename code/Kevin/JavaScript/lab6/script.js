const app = Vue.createApp({
    data(){
        return{
            message: 'Hello World',
            triviaResponse: {},
            seen: true,
            been: false,
            question: '',
            answers: [],
            score: 0,
            questionCounter: 0,
            transitionState: true,
            correct: '',
            correctAnswer : '',
        }
    },
    methods: {

        toggleSeen(){
            this.seen = !this.seen
            this.questionCounter++
        },

        continueGame(userAnswer){
            if (userAnswer === triviaResponse[this.questionCounter-1].correct_answer)
            {
                this.score++
                this.correctAnswer = ''
                console.log('SCORE!', this.score)
                this.correct = true
            }
            else
            {
                console.log('NOOO')
                this.correctAnswer = triviaResponse[this.questionCounter-1].correct_answer
                this.correct = false
            }
            if (this.questionCounter < 10)
            {
                this.transitionState = !this.transitionState
            }
            else
            {
                this.transitionState = 'game_over'
                return
            }
            console.log('continue game works')
            this.questionCounter++
            this.question = triviaResponse[this.questionCounter-1].question
            this.answers = triviaResponse[this.questionCounter-1].incorrect_answers
            this.answers.push(triviaResponse[this.questionCounter-1].correct_answer)
            this.answers = shuffle(this.answers)

        },

        onEnter(){
            document.querySelector('#hidden-text').innerHTML = ''
        },

        onLeave(){
            document.querySelectorAll('.play_buttons').forEach(element => {
                element.disabled = true
            });
            if (this.correct === true)
            {
                document.querySelector('#hidden-text').innerHTML = 'Correct!'
            }
            else if (this.correct === false)
            {
                document.querySelector('#hidden-text').innerHTML = `Nope. It was "${this.correctAnswer}."`
            }
            else
            {
                document.querySelector('#hidden-text').innerHTML = ''
            }
        },

        convertHTML(question){
            let txt = document.createElement("textarea")
            txt.innerHTML = question
            return txt.value
        },
        

        getData(){
            axios({
                method: 'get',
                url: 'https://opentdb.com/api.php',
                params:{
                    amount: 10,
                    type: 'multiple'
                }
              }).then((response) => {
                triviaResponse = response.data.results
                console.log(triviaResponse)
                this.question = triviaResponse[0].question
                this.answers = triviaResponse[0].incorrect_answers
                this.answers.push(triviaResponse[0].correct_answer)
                console.log(this.question)
                console.log(this.answers, typeof this.answers)
                console.log(shuffle(this.answers))
                this.answers = shuffle(this.answers)
                
              })
        }
    },
    setup(){
    }
})

function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex != 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
  }

