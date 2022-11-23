const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            currentUser: {},
            csrfToken: "",
            movies: [],
            newMovie: {
                'title': '',
                'director': '',
                'genre': '',
                'release_date': '',
                'rating': '' 
            }
        }
    },
    methods: {
        loadMovies(){
            axios({
                method: 'get',
                url: 'api/v1/movies'
            }).then(response => this.movies = response.data)
        },
        createMovie(){
            axios({
                method: 'post',
                url: 'api/v1/movies/',
                Headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    'title': this.newMovie.title,
                    'director': this.newMovie.director,
                    'genre': this.newMovie.genre,
                    'release_date': this.newMovie.release_date,
                    'rating': this.newMovie.rating
                }
            }).then(response => {
                this.loadMovies()
                this.newMovie.title = ""
                this.newMovie.director = ""
                this.newMovie.genre = ""
                this.newMovie.release_date = ""
                this.newMovie.rating = ""
            }).catch(error => {
                console.log(error.response.data)
            })
        },
    loadCurrentUser(){
        axios({
            method: 'get',
            url: '/users/currentuser/'
        }).then(response => {
            this.currentUser = response.data
        })
    }
    },
    created: function() {
        this.loadMovies()
        this.loadCurrentUser()
    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})