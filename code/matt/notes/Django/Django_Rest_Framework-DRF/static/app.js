
const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            message: 'hello world',

            currentUser: {},
            csrfToken: '',
            books: [],
            newBook: {
                "title" : "",
                "author": "",
                "genre": "",
                'isbn': ""
            }
        }
    },
    methods: {
        loadBooks(){
            axios({
                method: 'get',
                url: 'api/v1/books'
            }).then(response => {
                this.books = response.data
                console.log(response.data)
                }
            )
        },
        createBook() {
            
            axios({
                method: 'post',
                url: '/api/v1/books/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "title" : this.newBook.title,
                    "author": this.currentUser.id,
                    "genre": this.newBook.genre,
                    "isbn": this.newBook.isbn,
                }
            }).then( response => {
                this.loadBooks()
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
        this.loadBooks()
        this.loadCurrentUser()
    },
    mounted(){
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
      
       
    }
})

