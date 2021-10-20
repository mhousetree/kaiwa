<template>
  <div class="hello">
    <form @submit.prevent>
      <input type="text" v-model="get_key" />
      <input @click="get_data" type="button" value="GET" />
    </form>
    <p>
      <router-link v-if="result" v-bind:to="'/from/' + from_language + '/to/' + to_language + '/' + result.slug">Go!</router-link>
    </p>
    <p>{{ result.jp }}</p>
    <p>{{ result.en }}</p>
    <p>{{ result.ru }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data() {
    return {
      get_key: "",
      result: ""
    };
  },
  methods: {
    get_data() {
      axios
        .get("http://127.0.0.1:8000/expression/", {
          params: {
            key: this.get_key
          }
        })
        .then(
          function(response) {
            this.result = response.data;
            console.log(response);
          }.bind(this)
        )
        .catch(
          function(error) {
            this.result = "GETエラー";
            console.log(error);
          }.bind(this)
        );
    },
  },
  computed: {
    from_language () {
      return this.$store.state.from_language
    },
    to_language () {
      return this.$store.state.to_language
    }
  }
};
</script>