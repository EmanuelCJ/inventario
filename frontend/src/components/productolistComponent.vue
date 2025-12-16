<template>
  <form @submit.prevent="handleSubmit">
    <h1>LOGIN</h1>

    <div>
      <label>Username:</label>
      <input type="text" v-model="username" />
    </div>

    <div>
      <label>Password:</label>
      <input type="password" v-model="password" />
    </div>

    <button type="submit">Login</button>
  </form>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const username = ref("");
const password = ref("");

axios.defaults.withCredentials = true; // 👈 CLAVE

const handleSubmit = async () => {
  try {
    const res = await axios.post("http://127.0.0.1:5000/auth/login", {
      username: username.value,
      password: password.value
    });

    console.log("Login OK", res.data);
    // router.push("/dashboard")
  } catch (err) {
    console.error("Login error", err.response?.data);
  }
};
</script>
