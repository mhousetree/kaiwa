<template>
  <div class="expression">
    <h2>{{ result[from_language] }}</h2>
    <p>{{ result[to_language] }}</p>
    <!-- <audio
      v-bind:src="
        '/audio/' +
        category_id_to_slug(result.category_id) +
        '/' +
        to_language +
        '/' +
        $route.params.expression_slug +
        '.mp3'
      "
      controls
    ></audio> -->
  </div>
</template>

<script>
import axios from "axios";

// @ is an alias to /src
export default {
  name: "Expression",
  data() {
    return {
      result: "",
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/expression/", {
        params: {
          key: this.$route.params.expression_slug,
        },
      })
      .then(
        function (response) {
          this.result = response.data;
          console.log(response);
          document.querySelector("footer audio").src =
            "/audio/" +
            this.category_id_to_slug(this.result.category_id) +
            "/" +
            this.$store.state.to_language +
            "/" +
            this.$route.params.expression_slug +
            ".mp3";
        }.bind(this)
      )
      .catch(
        function (error) {
          this.result = "GETエラー";
          console.log(error);
        }.bind(this)
      );
    this.$store.watch(
      (state, getters) => getters.getToLanguage,
      (newValue, oldValue) => {
        console.log("to_language is changed: %s -> %s", oldValue, newValue);
        document.querySelector("footer audio").src =
          "/audio/" +
          this.category_id_to_slug(this.result.category_id) +
          "/" +
          this.$store.state.to_language +
          "/" +
          this.$route.params.expression_slug +
          ".mp3";
      }
    );
  },
  computed: {
    to_language() {
      return this.$store.state.to_language;
    },
    from_language() {
      return this.$store.state.from_language;
    },
  },
  methods: {
    category_id_to_slug(id) {
      const categories = [
        "dummy",
        "greetings",
        "airport",
        "change",
        "sightseeing",
        "transportation",
        "hotel",
        "restaurant",
        "shopping",
        "post_telephone",
        "trouble",
      ];
      return categories[id];
    },
  },
};
</script>

<style lang="scss" scoped>
.expression {
  height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  h2 {
    color: grey;
    margin-bottom: 1rem;
  }
  p {
    font-size: 2rem;
  }
}
</style>