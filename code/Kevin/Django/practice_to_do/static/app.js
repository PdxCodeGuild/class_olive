const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            currentUser: {},
            csrfToken: '',
            toDo: [],
            newToDo: {
                "item" : "",
                "needs_doing": "",
            },
            enteredThing: ''
        }
    },
    methods: {
        loadToDo(){
            axios({
                method: 'get',
                url: 'api/v1/todo'
            }).then(response => {
                this.toDo = response.data
                console.log(response.data)
                }
            )
        },
        createToDo() {
            
            axios({
                method: 'post',
                url: '/api/v1/todo/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "item" : this.enteredThing,
                    "author": this.currentUser.id,
                }
            }).then( response => {
                this.loadToDo()
                console.log(response.data)
            }).catch(error => {
                console.log(error.response)
             
            })

        },
        loadCurrentUser(){
            axios({
                method: 'get',
                url: '/users/currentuser/'
            }).then(response => {
                console.log('CU', response.data)
                this.currentUser = response.data
            }).catch(error =>{
                console.log(error.response)
            })
        },
        swapparo(id, currentBool){
            axios({
                method: 'patch',
                url: '/api/v1/todo/' + id + '/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "needs_doing": !currentBool
                }
            }).then(response => {
                // console.log(response.data)
                this.loadToDo()
            })
        },
        testFunc(){
            console.log(this.enteredThing)
        }

    },
    created: function() {
        this.loadToDo()
        this.loadCurrentUser()
    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
        console.log('mounted')
      
       
    }
})