
        //const app = Vue.createApp({})
        const {createApp} = Vue
        const miApp = createApp({
            data(){
                return {
                    saludo: "Hola ",
                    nombre: "Codo a Codo"
                }
            }




        })

        miApp.mount("#app")
