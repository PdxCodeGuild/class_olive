const app = Vue.createApp({
    data(){
        return{
            people: [
                {
                    id: 1,
                    name: 'tim',
                    state: 'oregon'
                },
                {
                    id: 2,
                    name: 'sarah',
                    state: 'florida'
                },
                {
                    id: 3,
                    name: 'jim',
                    state: 'washington'
                },
                {
                    id: 4,
                    name: 'chris',
                    state: 'florida'
                },
                {
                    id: 5,
                    name: 'tammy',
                    state: 'texas'
                },
                {
                    id: 6,
                    name: 'bob',
                    state: 'georgia'
                }  
            ],
            subject : '',
            searchSubject: '',
            displaySubject: ''
        }
    },
    methods: {
        getState(person){
            this.subject = `${person.name}, id: ${person.id} state: ${person.state}`
        },

        findSubject(){
            console.log(this.searchSubject)

            for(let i = 0; i < this.people.length; i++)
            {
                if(this.people[i].name === this.searchSubject)
                {
                    this.displaySubject = `${this.people[i].name}, id: ${this.people[i].id} state: ${this.people[i].state}`
                    return 
                }
            }
            this.displaySubject = this.searchSubject + ' is not in the database'
        }
    },
    setup(){
        console.log('this app mounted')
    }
})
