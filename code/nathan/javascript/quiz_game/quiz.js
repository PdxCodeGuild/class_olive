const app = Vue.createApp({
    data(){
        return{
            questions: [],
            grade : '',
            graded: false,
            firstTime: true,
            started: false,
            difficulty: 'easy',
            category: 18
        }
    },
    methods: {
        getData(){
            axios({
                method: 'get',
                url: 'https://opentdb.com/api.php',
                params: {
                    amount: 10,
                    category: this.category,
                    difficulty: this.difficulty,
                    type: 'multiple'
                }
            }).then((response) => {
                this.questions = []
                this.grade = ''
                this.graded = false
                this.started = true
                this.firstTime = false
                const badList = [/&quot;/gi, /&#039;/gi, /&#32;/gi, /&#33;/gi, /&#34;/gi, /&#35;/gi, /&#37;/gi, /&#44;/gi, /&#45;/gi, /&#46;/gi, /&#47;/gi]
                let id = 0
                for (x of response.data.results){
                    let item = {id: ++id, question: x.question}
                    item['answer'] = x.correct_answer
                    x.incorrect_answers.push(x.correct_answer)
                    item['options'] = x.incorrect_answers              
                    for(word of badList) {
                        item['question'] = item['question'].replace(word, "")
                        item['answer'] = item['answer'].replace(word, "")
                        item['options'][0] = item['options'][0].replace(word, "")
                        item['options'][1] = item['options'][1].replace(word, "")
                        item['options'][2] = item['options'][2].replace(word, "")
                        item['options'][3] = item['options'][3].replace(word, "")
                    }
                    item['options'].sort((a, b) => 0.5 - Math.random())
                    item['clicked'] = false
                    this.questions.push(item)
                }
            })
        },
        checkAnswer(questionID, option){
            for (question of this.questions) {
                if (question.id === questionID) {
                    question.clicked = true
                    if(question['answer'] === option){
                        question['wasCorrect'] = true
                    }
                    else{
                        question['wasCorrect'] = false
                    }
                }
            }
        },
        gradeQuiz(){
            this.graded = true
            let correct = 0 
            let incorrect = 0
            for (question of this.questions) {
                question.clicked = false
                if(question.wasCorrect){
                    correct++
                }
                else{
                    incorrect++
                }
            }
            let grade = 0
            if (correct > 0) {
                grade = ( correct / (correct + incorrect)) * 100
            }
            this.grade = `You got ${correct} questions right. ${incorrect} questions wrong. You made a ${grade}%`
        },
        onChangeDifficulty($event) {
            this.difficulty = $event.target.value
        },
        onChangeCategory($event) {
            this.category = $event.target.value
        }
 }
})