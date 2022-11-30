
const app = Vue.createApp({
    delimiters: ['[[',']]'],
    data(){
        return{
            
            csrfToken: '',
            currentUser: {},
            message: `Welcome`,

            movie: [],
            newMovie: {
                title: '',
                genre: ''
            }
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
        loadCurrentUser(){
            axios({
                method: 'get',
                url: '/users/currentuser'
            }).then(response => {
                console.log(response.data)
                this.currentUser = response.data
            })
        }


    },
    created: function(){
        this.loadMovies()
        this.loadCurrentUser()
        console.log('created')
        


    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value        
        
    }


})