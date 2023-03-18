const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            currentUser: {},
            csrfToken: "",
            newMovie: {
                'title': '',
                'have_watched': false,
                'rating': '' 
            },
            status: ""
        }
    },
    methods: {
        deleteMovie(){
            const theMovieID = document.querySelector('#theMoviesID')
            axios({
                method: 'delete',
                url: `../../api/v1/movies/${theMovieID.innerHTML}`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                }
            }).then( response => {
                this.status = "was deleted."
            }).catch(error => {
                console.log(error.response)
                this.status = ""
            })
        },
        updateMovie(){
            const theMovieID = document.querySelector('#theMoviesID')
            const theMoviesTitle = document.querySelector('#theMoviesTitle')
            axios({
                method: 'put',
                url: `../../api/v1/movies/${theMovieID.innerHTML}/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {                   
                    'title': theMoviesTitle.innerHTML,
                    'have_watched': this.newMovie.have_watched,  
                    'rating': this.newMovie.rating,
                    'movie_user': this.currentUser.id                                                   
                }
            }).then( response => {
                this.status = "was updated."
            }).catch(error => {
                console.log(error.response.data)
                this.status = ""
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
        this.loadCurrentUser()  
    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})