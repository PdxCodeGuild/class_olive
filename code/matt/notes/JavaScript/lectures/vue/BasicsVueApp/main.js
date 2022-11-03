const app = Vue.createApp({
    data(){
        return{
            message: 'Hello World',
            arrayCounter : 0,
            arrayOfMessages: [
                'Goodbye World!',
                'Eat Pizza',
                'Tacos Taste like Tacos',
                'GOW',
                'Hello World',
            ],
            colors: [
                'red',
                'blue',
                'green',
                'error',
                'gold',
                'teal',
                'purple'
            ],
            name : ''

        }
    },
    methods: {
        changeText(){
            // this.message = 'Goodbye World!'

            this.message = this.arrayOfMessages[this.arrayCounter]
            this.arrayCounter++

            if (this.arrayOfMessages.length === this.arrayCounter)
            {
                this.arrayCounter = 0
            }
        }
    },
    setup(){
        console.log('this app mounted')
    }
})
