const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            currentUser: {},
            csrfToken: '',
            toDo: [],
            newToDo: {
                "item" : "",
                "author": "",
                "needs_doing": "",
            }
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
                    "item" : this.newToDo.item,
                    "author": this.currentUser.id,
                    "needs_doing": this.newToDo.needs_doing,
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
            })
        }

    },
    created: function() {
        this.loadToDo()
        this.loadCurrentUser()
    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
      
       
    }
})