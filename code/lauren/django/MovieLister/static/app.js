
const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            currentUser: {},
            csrfToken: '',
            movies: [],
            newMovie: {
                "title" : "",
                "director": "",
                "genre": "",
                "release_date": "",
                "opinion": "",
                "likes": "",
                // "poster": ""
            }
        }
    },
    methods: {

        loadMovies(){
            axios({
                method: 'get',
                url: 'api/v1/movies'
            }).then(response => {
                this.movies = response.data
                console.log(response.data)
                }
            )
        },
        createMovie() {
            // let posterImg = document.querySelector('#movie-input').files[0].name
            // console.log(posterImg)
            axios({
                method: 'post',
                url: '/api/v1/movies/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "title" : this.newMovie.title,
                    "author": this.currentUser.id,
                    "director": this.newMovie.director,
                    "genre": this.newMovie.genre,
                    "release_date": this.newMovie.release_date,
                    "opinion": this.newMovie.opinion,
                    // "poster": posterImg
                    
                }
            }).then( response => {
                this.loadMovies()
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
                this.currentUser = response.data
            }).catch(error =>{
                console.log(error)
            })

        },


        createLikes(movie) {
            axios({
                method: 'put',
                url: `/api/v1/movies/${movie.id}/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: { 
                    "id": movie.id,
                    "title": movie.title,
                    "genre":  movie.genre,
                    "director": movie.director,
                    "release_date":  movie.release_date,
                    "opinion": movie.opinion,
                    "author_detail": {
                        "id": movie.author_detail.id,
                        "username": movie.author_detail.username,
                    },
                    "author": movie.author,
                    "likes": movie.likes +1
                }
            }).then(response => {
                this.loadMovies()

                console.log(response.data)
            })


    },

        displayinfo(index){
            document.querySelector("#id" + index).style.display = "block"
        },


        hideinfo(index){
            document.querySelector("#id" + index).style.display = 'none'
        }
},




    created: function() {
        this.loadCurrentUser()
        this.loadMovies()
    },
    mounted(){
       this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
        
       
    }
})