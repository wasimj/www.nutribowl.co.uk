<template>
  <div class="min-h-screen bg-cover flex flex-col">
    <!-- Hero Section -->
    <section class="flex-1 flex items-center justify-center bg-blue-500 text-white bg-hero-pattern bg-cover bg-center">
      <div class="text-center">
        <h1 class="text-4xl font-bold mb-2">Nutribowl</h1>
        <p class="mb-4">Nutritious, Tasty, Quick</p>
        <p class="mb-4">Pick Three!</p>
      </div>
    </section>

    <!-- Menus Section -->
    <section class="flex-1 flex flex-col items-center p-10 bg-gray-100 text-gray-800">
      <h2 class="text-3xl font-bold mb-6">Menus</h2>
      <div class="flex flex-wrap justify-center gap-4">

        <div class="bg-white shadow-lg rounded-lg p-6 w-80 transition duration-300 ease-in-out hover:shadow-xl hover:scale-105" v-for="recipe in recipes" :key="recipe.id">
          <h3 class="font-semibold text-xl">{{ recipe.name }}</h3>
          <p></p>
        </div>

      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-blue-800 text-white text-center p-4">
      © 2024 Nutribowl Ltd
    </footer>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      recipes: []  // This will hold the array of recipes
    };
  },
  created() {
    this.fetchRecipes();  // Fetch the recipes when the component is created
  },
  methods: {
    fetchRecipes() {
      axios.get('http://localhost:8001/recipes')
        .then(response => {
          console.log('Recipes: ', this.recipes)
          this.recipes = response.data.recipes;  // Access the recipes property from the JSON response
        })
        .catch(error => {
          console.error('There was an error fetching the recipes:', error);
        });
    }
  }
}
</script>


<style>
/* Custom CSS */
html, body {
  height: 100%;
  margin: 0;
  color: white;
  font-family: Arial, sans-serif;
  text-align: center;
}
body {
  background: url('/img/Background.png') no-repeat center center fixed;
  background-size: cover;
}


</style>
