<template>
  <div class="columns">
    <div class="column is-one-fifth">
      <SidebarMenu />
    </div>
    <div class="column">
      <router-view />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SidebarMenu from "@/components/SidebarMenu.vue";
export default defineComponent({
  components: {
    SidebarMenu,
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #3176bc;
}
body {
  background-color: #cbffc6;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
