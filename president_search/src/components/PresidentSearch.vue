<template>
    <div class="container">
      <div class="top-bar">
        <span class="logo">Intuitive Care</span>
      </div>
      <div class="header">
        <h4>TESTES DE NIVELAMENTO v.250321</h4>
        <p>Assis Berlanda de Medeiros</p>
        <h1>Busca de Presidentes</h1>
      </div>
      <button @click="fetchData" class="search-button">Buscar Dados</button>
      <div v-if="data.length" class="data-list">
        <ul>
          <li v-for="item in data" :key="item.id" class="data-item">
            {{ item }}
          </li>
        </ul>
      </div>
      <p v-if="error" class="error-message">
        {{ error }}
      </p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        data: [],
        error: null,
      };
    },
    methods: {
      async fetchData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/buscar_presidente');
          this.data = response.data;
          this.error = null;
        } catch (err) {
          this.error = 'Erro ao buscar os dados. Por favor, tente novamente.';
          this.data = [];
        }
      },
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
  
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-height: 100vh;
    background-color: #f4f7f9;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 20px;
  }
  
  .top-bar {
    width: 100%;
    display: flex;
    justify-content: flex-start;
    padding: 10px 20px;
    background-color: #F2F2F2; /* Cor de fundo suave para a barra superior */
    border-bottom: 1px solid #b0bec5; /* Adiciona uma borda inferior para separar visualmente */
    box-sizing: border-box; /* Garante que o padding não afete a largura total */
  }
  
  .logo {
    font-size: 1.2em;
    font-weight: bold;
    color: #34495e; /* Cor do texto do logo */
    font-family: 'Montserrat', sans-serif;
  }
  
  .header {
    margin-bottom: 30px;
    text-align: center;
    width: 100%; /* Garante que o cabeçalho ocupe toda a largura */
  }
  
  h1 {
    color: #0D0D0D;
    font-size: 2.5em;
    margin-bottom: 10px;
    font-family: 'Montserrat', sans-serif;
  }
  
  h4,
  p {
    color: #0D0D0D;
    margin-bottom: 10px;
    font-family: 'Montserrat', sans-serif;
  }
  
  .search-button {
    padding: 12px 25px;
    background-color: #c8a4f4;
    color: #0d0d0d;
    border: 2px solid #0d0d0d;
    border-radius: 5px;
    font-size: 1em;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .search-button:hover {
    background-color: #0d0d0d;
    color: #c6a7f2;
  }
  
  .data-list {
    margin-top: 30px;
    width: 80%;
    max-width: 600px;
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  .data-item {
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: left;
  }
  
  .error-message {
    color: #e74c3c;
    margin-top: 20px;
    font-weight: bold;
  }
  </style>