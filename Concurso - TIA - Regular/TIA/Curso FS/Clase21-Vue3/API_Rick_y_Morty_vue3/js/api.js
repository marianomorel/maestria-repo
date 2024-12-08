const { createApp } = Vue  //creo un objeto VUE llamdo createApp

// const app = Vue.createApp({
createApp({
        data() {
    return {
        // https://rickandmortyapi.com/api/character/247
        url: 'https://rickandmortyapi.com/api/character/',
        personajes: []
        }
    },
    methods: {
        async fetchData(url) {
            const res = await fetch(url);
            data = await res.json();
            // console.log(data.results);
            this.personajes = data.results;
            }
    },
    async created() {
        await this.fetchData(this.url)
    }
}).mount('#app')
