<template>
  <div>
    <h1>Associations View</h1>
    <AssociationCard association="association" />
    <AssociationCard association="association" />
    <AssociationCard association="association" />
    <AssociationCard association="association" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AssociationCard from "@/components/AssociationCard.vue";
export default defineComponent({
  name: "AssociationsView",
  components: {
    AssociationCard,
  },
  data() {
    return {
      association: {
        name: "Association 1",
        image: "../assets/head.jpg",
      },
    };
  },
});
</script>
