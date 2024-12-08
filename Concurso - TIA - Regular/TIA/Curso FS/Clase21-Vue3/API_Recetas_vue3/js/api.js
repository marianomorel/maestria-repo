const { createApp } = Vue  //creo un objeto VUE llamdo createApp
const miApp = createApp({
  data() {
    return {
      url: 'https://api.sampleapis.com/recipes/recipes',
      recipesAll: [],
      recipes: [],
      cuisines: [],
      cursos: [],
      calories: 1000,
      cuisine: "All",
      curso: "All"
    }
  },

  methods: {
    async fetchData(url) {
      resp = await fetch(url)
      this.recipesAll = await resp.json()
      this.recipes = this.recipesAll
    },

    filtro() {
      this.recipes = this.recipesAll.filter(elemento => (elemento.calories <= this.calories && elemento.calories != "") && (elemento.cuisine == this.cuisine || this.cuisine === "All") && (elemento.course == this.curso || this.curso === "All"))
    },
    orden() {
      this.recipes.sort((a, b) => { return (a.title > b.title ? 1 : -1) })// si retorna 1 lo invierte, si retorna -1 lo deja como esta 
    },
    cargarListasDesplegables() {
      this.cuisines = ['All']
      this.cursos = ['All']
      for (elemento of this.recipesAll) {
        if (elemento.cuisine !== '' && this.cuisines.indexOf(elemento.cuisine) < 0) {
          this.cuisines.push(elemento.cuisine)
        }
        if (elemento.course !== '' && this.cursos.indexOf(elemento.course) < 0) {
          this.cursos.push(elemento.course)
        }
      }
    }
  },

  async created() {
    await this.fetchData(this.url)
    this.cargarListasDesplegables()
  }
})

miApp.mount('#app')

