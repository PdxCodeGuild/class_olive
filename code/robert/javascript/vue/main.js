const app = Vue.createApp({
    data(){
        return{
            toDo:[{
                task: 'Dishes',
                complete: false
            },{
                task: 'Feed Fish',
                complete: true
            },
            ],    
            newTask: ''
        }
    },
    methods: {
        submitTask(){
            let newTaskData = {
                task: this.newTask,
                complete: false,
            }
            this.toDo.unshift(newTaskData)
        },
        deleteTask(removeTask){
            this.toDo.forEach(task =>{
                    if (task === removeTask){
                        this.toDo.splice(this.toDo.indexOf(task),1)
                    }
            }
            )
        },
        completed(task){
            task.complete = !task.complete
        }
    },
    setup(){
        console.log("Running!")
    }
})