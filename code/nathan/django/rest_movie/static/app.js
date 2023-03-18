const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            currentUser: {},
            csrfToken: "",
            movies: [],
            newMovie: {
                'title': '',
                'have_watched': false,
                'rating': '' 
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
                this.getMovieDetails()
                })
        },
        createMovie(){
            axios({
                method: 'post',
                url: 'api/v1/movies/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    'title': this.newMovie.title,
                    'have_watched': this.newMovie.have_watched,
                    'rating': this.newMovie.rating,
                    'movie_user': this.currentUser.id
                }
            }).then(response => {
                this.loadMovies()
                this.newMovie.title = ""
                this.newMovie.have_watched = false
                this.newMovie.rating = ""
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        deleteMovie(id){
            axios({
                method: 'delete',
                url: `api/v1/movies/${id}`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                }
            })
        },
        updateMovie(id){
            axios({
                method: 'put',
                url: `api/v1/movies/${id}`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    'have_watched': this.newMovie.have_watched,
                    'rating': this.newMovie.rating
                }
            })

        },
        getMovieDetails(){
            for(let i = 0; i < this.movies.length; i++) {       
                this.movies[i]['hover'] = false     
                movieTitle = this.movies[i].title.replace(" ", "%20")
                axios({
                    method: 'get',
                    url: `https://api.themoviedb.org/3/search/movie?api_key=c77c935cf08ab8be04818ab351bd382f&language=en-US&query=${movieTitle}&page=1&include_adult=false`
                }).then(response => {
                    response = response['data']['results'][0]
                    this.movies[i]['apiDetails'] = response
                    posterPath = response['poster_path']
                    posterPath = `https://image.tmdb.org/t/p/w500/${posterPath}`
                    this.movies[i]['posterPath'] = posterPath
                })
            }
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