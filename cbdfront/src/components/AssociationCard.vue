<template>
  <div class="card">
    <div class="card-content">
      <div class="media">
        <div class="media-left">
          <figure class="image is-48x48">
            <img :src="association.image" alt="Association Image" />
          </figure>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "AssociationCard",
  props: {
    association: {
      type: Object,
      required: true,
    },
  },
});
</script>
