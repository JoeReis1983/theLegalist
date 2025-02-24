<template>
  <section class="section">
    <div class="container">
      <h1 class="title">Bem-vindo ao Vue com Bulma!</h1>
      <p class="subtitle">Um framework CSS moderno e fácil de usar.</p>
      <button class="button is-primary">Botão Primário</button>
      <button class="button is-link">Botão Link</button>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "HomeView",
});
</script>
