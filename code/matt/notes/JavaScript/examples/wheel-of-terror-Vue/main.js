const app = Vue.createApp({
    data(){
        return{
            delayVar : .1,
            students : ['robert', 'kevin', 'tim', 'nathan', 'lauren']
        }
    },
    methods: { 
        animate(){
            this.resetVariablesAndNodes()
            
            let numberOfCycles = this.getNumberOfCycles()
            let cycleCounter = 0
            let chosenStudentIndex = this.getChosenStudentIndex()

            // console.log("Number of cycles to be ran:", numberOfCycles)

            // while cycleCounter is not equal to numberOfCycles
            while (true){

                for (let i = 0; i < this.students.length ; i++){
                    gsap.to(`#${this.students[i]}`, {delay: this.delayVar, color: 'red'})
                    this.resetOtherStudentsColor(i)
                    this.delayVar += .2
                }
                cycleCounter++

                // do a final loop to show the 'winner' and stop on the index of the student who won
                if (cycleCounter === numberOfCycles){
                    
                    for (let i = 0; i < chosenStudentIndex ; i++){
                        gsap.to(`#${this.students[i]}`, {delay: this.delayVar, color: 'red'})
                        this.resetOtherStudentsColor(i)
                        this.delayVar += .2
                    }
                    console.log('we reached the end of the while loop')
                    break
                }

            }
        },


        getNumberOfCycles(){
            return parseInt(Math.random() * (5 - 1) + 1)
        },

        getChosenStudentIndex(){
            return parseInt(Math.random() * (this.students.length - 0) + 0)
        },

        resetOtherStudentsColor(i){
            // if first student, make last white
            if (i == 0){
                gsap.to(`#${this.students[4]}`, {delay: this.delayVar, color: 'white'})
            }
            else{
                gsap.to(`#${this.students[i -1]}`, {delay: this.delayVar, color: 'white'})
            }
        },

        resetVariablesAndNodes(){
            this.delayVar = .1
            
            for (let i = 0; i < this.students.length ; i++){
                gsap.to(`#${this.students[i]}`, {delay: 0, duration: 0, color: 'white'})
            }
        }



    },
    mounted(){
        // console.log(this.students[1])

        // let delayVar = 0

        // for (let i = 0; i < this.students.length; i++){
        //     gsap.to(`#${this.students[i]}`, {delay: delayVar, color: 'red'})
        //     delayVar++
        // }

    }
})
