const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            currentUser: {},
            csrfToken: '',
            toDo: [],
            displayedToDo: [],
            displayedFavorites: [],
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
                console.log( 'from loadToDo', typeof this.toDo, this.toDo)
                this.displayedToDo = []
                for (i=0; i < this.toDo.length; i++){
                    this.displayedToDo.push(this.toDo[i].item)
                    console.log(this.toDo[i].item)
                }
                console.log('displayed todo',this.displayedToDo)
                this.loadCurrentUser()
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
                this.enteredThing = ''
                this.loadToDo()
                console.log(response.data)
            }).catch(error => {
                console.log(error.response)
             
            })

        },
        deleteToDo(id){
            axios({
                method: 'delete',
                url: '/api/v1/todo/' + id,
                headers: {
                    'X-CSRFToken': this.csrfToken
                }
            }).then(response => {
                console.log('workin')
                this.loadToDo()
            })
        },
        createFavorite(item){
            axios({
                method: 'post',
                url: '/api/v1/favorites/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "favorite" : item,
                    "author": this.currentUser.id,
                }
            }).then(response => {
                this.loadToDo()
                console.log(response.data)
            }).catch(error => {
                console.log(error.response)
            })
        },
        spawnFromFavorites(item){
            axios({
                method: 'post',
                url: '/api/v1/todo/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "item" : item,
                    "author": this.currentUser.id,
                }
            }).then( response => {
                this.loadToDo()
                console.log(response.data)
            }).catch(error => {
                console.log(error.response)
             
            })
        },

        deleteFavorite(id){
            axios({
                method: 'delete',
                url: '/api/v1/favorites/' + id,
                headers: {
                    'X-CSRFToken': this.csrfToken
                }
            }).then(response => {
                console.log('workin')
                this.loadToDo()
            })
        },



        loadCurrentUser(){
            axios({
                method: 'get',
                url: '/users/currentuser/'
            }).then(response => {
                console.log('CU', response.data)
                this.displayedFavorites = []
                for (i=0;i < response.data.favorites_detail.length; i++){
                    this.displayedFavorites.push(response.data.favorites_detail[i].favorite)
                }
                console.log('displayed favs',typeof this.displayedFavorites, this.displayedFavorites)
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
        
    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
        console.log('mounted')
      
       
    }
})