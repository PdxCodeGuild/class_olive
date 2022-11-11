const app = Vue.createApp({
    data(){
        return{
            toDoList:[
                {
                    item: 'take trash out',
                    isComplete: false
                },
                {
                    item: 'vacuum',
                    isComplete: true
                },
            ],
            newItem: ''
        }
    },
    methods: {
        swappem(item){
            item.isComplete = !item.isComplete
        },
        submitItem(){
            let itemTemplate = {
                item: this.newItem,
                isComplete: false,
            }


            this.toDoList.unshift(itemTemplate)
        },
        deleteItem(itemToDelete){
            this.toDoList.forEach(item =>
                {
                    if (item === itemToDelete)
                    {
                        this.toDoList.splice(this.toDoList.indexOf(item),1)
                    }
                })
        }
    },
    setup(){
    }
})