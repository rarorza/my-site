<script setup>
const props = defineProps({
  educationOrJob: String
})

</script>

<template>
  <!-- education_content && experience_content -->
  <div :class="props.educationOrJob">
    <div class="activated">
      <span>XXXX-202X</span>
      <h3>title</h3>
      <p>description</p>
    </div>
    <ul>
      <li><i class="fa-sharp fa-solid fa-circle"></i></li>
    </ul>
  </div>
</template>