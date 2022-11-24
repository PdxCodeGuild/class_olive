const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            currentUser: {},
            csrfToken: '',
            movies: [],
            newMovie: {
                "title" : "",
                "genre": "",
                "year": "",
                'rating': "",
                'addedBy': "",
                'onNetflix': "",
                'onHulu': "",
                'onAmazon': "",
                'onHBO': "",
            }
        }
    },
    methods: {
        loadMovies(){
            axios({
                method: 'get',
                url: '../../api/v1/movies'
            }).then(response => {
                this.movies = response.data
                // console.log(response.data)
                }
            )
        },

        createMovie() {
            axios({
                method: 'post',
                url: '../../api/v1/movies/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "title" : this.newMovie.title,
                    "genre": this.newMovie.genre,
                    "year": this.newMovie.year,
                    "metacritic": this.newMovie.metacritic,
                    "addedBy": this.currentUser.id,
                    "onNetflix": this.newMovie.onNetflix,
                    "onHulu": this.newMovie.onHulu,
                    "onAmazon": this.newMovie.onAmazon,
                    "onHBO": this.newMovie.onHBO,
                }
            }).then(response => {
                this.loadMovies()
                console.log(response.data)
            }
            ).catch(error => {
                console.log(error.response.data)
            })
        },
        
        loadCurrentUser(){
            axios({
                method: 'get',
                url: '../../users/currentuser/'
            }).then(response => {
                // console.log('CU', response.data)
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

