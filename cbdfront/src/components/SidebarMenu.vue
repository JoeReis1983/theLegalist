<template>
  <div class="sidebar">
    <aside class="menu">
      <div class="menu-list">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/associations">Associações</router-link>
      </div>
    </aside>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "SidebarMenu",
  data() {
    return {
      isActive: false,
    };
  },
});
</script>

<style scoped>
.sidebar {
  padding: 1rem;
  background-color: #f5f5f5;
  min-height: 100vh;
  border-right: 1px solid #dbdbdb;
}

.menu-label {
  color: #4d175d;
  font-size: 0.75em;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 0.5em;
}

.menu-list a {
  color: #060606;
  padding: 0.5em 0.75em;
  background-color: transparent;
}

.menu-list a:hover {
  background-color: #06ff0e;
  color: #d71e1e;
}

.menu-list a.is-active {
  background-color: #3273dc;
  color: #fff;
}
</style>
