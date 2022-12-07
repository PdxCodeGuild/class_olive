
const app = Vue.createApp({
    delimiters: ['[[',']]'],
    data(){
        return{
            
            csrfToken: '',
            currentUser: {},
            message: ` `,

            movie: [],
            newMovie: {
                title: '',
                genre: ''
            },
            editTitle: '',
            editGenre: '',
        }
    },
    methods: {
        loadMovies(){
            axios({
                method: 'get',
                url: 'api/v1/movie'
            }).then(response => {
                this.movie = response.data
                console.log(this.movie)
                this.loadCurrentUser()
                }
            )
        },
        createMovie(){
            axios({
                method: 'post',
                url: 'api/v1/movie/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    title: this.newMovie.title,
                    director: this.currentUser.id,
                    genre: this.newMovie.genre
                }
            }).then(response => {
                console.log(response.data)
                this.newMovie = {
                    title: '',
                    genre: ''
                }
                console.log('wiped')
                this.loadMovies()
                
                }
            ).catch(error => {
                console.log(error.data)
            })
        },
        deleteMovie(id){
            axios({
                method: 'delete',
                url: '/api/v1/movie/' + id,
                headers: {
                    'X-CSRFToken': this.csrfToken
                }
            }).then(response => {
                console.log('workin')
                this.loadMovies()
            })
        },
        editMovie(id,){
            axios({
                method: 'patch',
                url: '/api/v1/movie/' + id + '/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "title": this.editTitle,
                    "genre": this.editGenre,
                }
            }).then(response => {
                // console.log(response.data)
                this.switchBackFromEdit()
                this.loadMovies()
            })
        },
        loadCurrentUser(){
            axios({
                method: 'get',
                url: '/users/currentuser'
            }).then(response => {
                console.log(response.data)
                this.currentUser = response.data
            })
        },
        switchToEdit(index, title, genre){
            document.querySelectorAll('.edit-button').forEach(element => {
                element.disabled = true
            })
            document.querySelector('#post-div'+ index).style.display = 'none'
            document.querySelector('#edit-div'+ index).style.display = 'block'
            this.editTitle = title
            this.editGenre = genre
            
        },
        switchBackFromEdit(){
            document.querySelectorAll('.edit-button').forEach(element => {
                element.disabled = false
            })
            document.querySelectorAll('.post-div').forEach(element => {
                element.style.display = 'block'
            })
            document.querySelectorAll('.edit-div').forEach(element => {
                element.style.display = 'none'
            })
        }


    },
    created: function(){
        this.loadMovies()
        console.log('created')
        


    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value        
        
    }


})