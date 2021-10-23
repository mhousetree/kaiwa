<template>
  <div class="settings">
    <h2>設定</h2>
    <!-- <dl id="expressions">
      <template v-for="expression in result" v-bind:key="expression.id">
        <dt>
          <router-link
            v-bind:to="
              '/from/' +
              from_language +
              '/to/' +
              to_language +
              '/' +
              expression.slug
            "
            >{{ expression[from_language] }}</router-link
          >
        </dt>
        <dd>
          <router-link
            v-bind:to="
              '/from/' +
              from_language +
              '/to/' +
              to_language +
              '/' +
              expression.slug
            "
            >{{ expression[to_language] }}</router-link
          >
        </dd>
      </template>
    </dl> -->
  </div>
</template>

<script>
import axios from "axios";

// @ is an alias to /src
export default {
  name: "Settings",
  data() {
    return {
      result: "",
    };
  },
  mounted() {
    const category_name_to_id = {
      greetings: 1,
      airport: 2,
      change: 3,
      sightseeing: 4,
      transportation: 5,
      hotel: 6,
      restaurant: 7,
      shopping: 8,
      post_telephone: 9,
      trouble: 10,
    };
    axios
      .get("http://127.0.0.1:8000/expressions-in-category/", {
        params: {
          key: category_name_to_id[this.$route.params.category],
        },
      })
      .then(
        function (response) {
          this.result = response.data;
        }.bind(this)
      )
      .catch(
        function (error) {
          this.result = "GETエラー";
          console.log(error);
        }.bind(this)
      );
  },
  computed: {
    from_language() {
      return this.$store.state.from_language;
    },
    to_language() {
      return this.$store.state.to_language;
    },
  },
  methods: {
    category_slug_to_id(slug) {
      const categories = {
        greetings: 1,
        airport: 2,
        change: 3,
        sightseeing: 4,
        transportation: 5,
        hotel: 6,
        restaurant: 7,
        shopping: 8,
        post_telephone: 9,
        trouble: 10,
      };
      return categories[slug];
    },
    category_id_to_jpname(id) {
      const categories = [
        "dummy",
        "基本表現",
        "空港",
        "両替",
        "観光",
        "交通",
        "宿泊",
        "食事",
        "買い物",
        "郵便・電話",
        "トラブル",
      ];
      return categories[id];
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../colors.scss";
h2 {
  font-size: 1.8rem;
  margin: 0.5em 0;
  font-weight: 400;
}

#expressions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  text-align: left;
  border: 1px solid mix($grey, $white);

  dt,
  dd {
    padding: 0.5rem;
    border-bottom: 1px dashed mix($grey, $white);

    &:last-of-type {
      border-bottom: none;
    }
  }

  dt {
    background-color: rgba($blue, 0.2);
  }

  dd a::before {
    content: "\e050";
    font-family: "Material Icons";
    color: $blue;
    margin-right: 0.3rem;
  }

  a {
    display: block;
    color: inherit;
    text-decoration: none;
  }
}

@media screen and (min-width: 630px) {
  #expressions {
    display: grid;
    grid-template-columns: repeat(2, 1fr);

    a {
      color: inherit;
      text-decoration: none;
    }
  }
}
@media screen and (max-width: 433px) {
  #expressions {
    dt,
    dd {
      border-bottom: none;
    }
  }
}
</style>