const app = Vue.createApp({
    data(){
        return{
            todos: [
                {
                    task: 'Work',
                    done: false

                },
                {
                    task: 'breathe',
                    done: true
                }

            ],
            task: '',
            index: 0
        };
    },
    
    methods: {
        add(){
            this.todos.push({
                task: this.task,
                done: false
            });
            this.task='';
        },
        deleteItem(index) {
            this.todos.splice(index, 1)
            console.log('hi')
    
        },

        toggleComplete(index){
            this.todos[index].done = !this.todos[index].done
        },

    setup(){

    }
}

})
