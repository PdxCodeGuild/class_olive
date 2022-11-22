const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            csrfToken: '',
            movies: [],
            newMovie: {
                "title" : "",
                "genre": "",
                "year": "",
                'rating': "",
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
            
            axios({
                method: 'post',
                url: 'api/v1/movies/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "title" : this.newMovie.title,
                    "genre": this.newMovie.genre,
                    "year": this.newMovie.year,
                    "metacritic": this.newMovie.metacritic,
                    "cover": this.newMovie.cover,
                }
            }).then( response => {
                this.loadMovies()
                console.log(response.data)
            }
            ).catch(error => {
                console.log(error.response.data)
            })
        }
    },
    
    created: function() {
        this.loadMovies()
    
    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})

