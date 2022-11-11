idCounter = 2

const app = Vue.createApp({
    data(){
        return{
            tasks: [
                {
                    'id': 1,
                    'name': 'Write tests for code',
                    'complete': false
                },
                {
                    'id': 2,
                    'name': 'Push code to repo',
                    'complete': false
                }
            ],
            task_name: ''
        }
    },
    methods: {
        addToDo(task_name){
            if(task_name !== undefined && task_name !== null && task_name !== "") {
                newTask = {'id': ++idCounter, 'name': task_name, 'complete': false}
                this.tasks.push(newTask)
                this.task_name = ""
            }
        },
        deleteToDo(task){
            for(let i = 0; i < this.tasks.length; i++){
                if (this.tasks[i].id === task.id){
                    this.tasks.splice(i, 1)
                }
            }
        },
        complete(completeTask){
            for(x of this.tasks){
                if (x === completeTask){
                    x.complete = true
                }
            }
        },
        unComplete(unCompleteTask){
            for(x of this.tasks){
                if (x === unCompleteTask){
                    x.complete = false
                }

            }
        },
        areThereTodos(){
            for(x of this.tasks){
                if(!x.complete){
                    return true
                }
            }
            return false
        },
        arethereCompleted(){
            for(x of this.tasks){
                if(x.complete){
                    return true
                }
            }
            return false
        },
        setup(){
            console.log('this app mounted')
        }
    }
})