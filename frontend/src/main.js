import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'

import 'bootstrap/dist/css/bootstrap.min.css'
import bootstrap from 'bootstrap'

// const app = createApp(App).mount('#app')

const app = createApp(App)
app.use(router)
app.mount('#app')
