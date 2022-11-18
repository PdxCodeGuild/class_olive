
const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
            message: 'hello world',

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
                    "author": this.newBook.author,
                    "genre": this.newBook.genre,
                    "isbn": this.newBook.isbn,
                }
            }).then( response => {
                this.loadBooks()
                console.log(response.data)
            }).catch(error => {
                console.log(error.response)
             
            })

        }

    },
    created: function() {
        this.loadBooks()
    },
    mounted(){
       this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
      
       
    }
})

