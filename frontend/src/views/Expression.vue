<template>
  <div class="home">
    <h2>{{ result[from_language] }}</h2>
    <audio v-bind:src="'/audio/greetings/' + to_language + '/' + $route.params.expression_slug + '.mp3'" controls></audio>
  </div>
</template>

<script>
import axios from "axios";

// @ is an alias to /src
export default {
  name: "Expression",
  data() {
    return {
      result: ""
    }
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/expression/", {
        params: {
          key: this.$route.params.expression_slug
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
      )
  },
  computed: {
    to_language () {
      return this.$store.state.to_language
    },
    from_language () {
      return this.$store.state.from_language
    }
  },
  methods: {

  }
};
</script>
