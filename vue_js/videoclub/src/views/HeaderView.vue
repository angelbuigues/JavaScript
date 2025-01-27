<script></script>
<template>
    <div id="header">
        <h1>
            blockbuster
        </h1>

        <nav>
            <li>
                <router-link to="/">🏠 Inicio</router-link>
            </li>
            <li>
                🎞️ TOP 10 Películas
            </li>
            <li>
                ℹ️ Acerca de BlockBuster
            </li>
            <li>
                📚 Contacto
            </li>
        </nav>
    </div>
</template>
<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Jersey+15&family=Nabla&display=swap');

    #header {
        text-align: center;
        border-bottom: dashed 4px rgb(49, 49, 49);
        padding: 20px 0;
    }

    nav {
        list-style-type: none;
        font-family: "Jersey 15";
        font-size: 1.2em;
        text-transform: uppercase;
        letter-spacing: 2px;

        display: grid;
        grid-template-columns: repeat(4, 1fr);
    }

    
    h1 {
        font-family: "Nabla", serif;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
        font-variation-settings:
          "EDPT" 100,
            "EHLT" 12;
        font-size: 3.5em;
        letter-spacing: 5px;

        text-shadow: 5px 3px 8px #3f3f3f;
        margin: 0 0 20px 0;
    }
</style>