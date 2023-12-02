const app = Vue.createApp({
  data: function () {
      return {
          title: 'NutriMade',
          nutri_info_1: 'Dieta Wegańska',
          nutri_info_2: 'Dieta Wegetariańska',
          nutri_info_3: 'Bez Laktozy',
          nutri_info_4: 'Cukrzyca',
          nutri_info_5: 'Kalorie',
          text: '',
          loading: false,
          vegan_diet: false,
          vegetarian_diet: false,
          no_lactose: false,
          Diabetes: false,
          Calories: '',
          Meal_type: '',
          Preferences: '',
      }
  },
  methods: {
      async sendNutriForm() {
          const requestData = {
              vegan_diet: this.vegan_diet,
              vegetarian_diet: this.vegetarian_diet,
              no_lactose: this.no_lactose,
              Diabetes: this.Diabetes,
              Calories: this.Calories,
              Meal_type: this.Meal_type,
              Preferences: this.Preferences,
          };

          this.loading = true;

          const response = await fetch(`http://127.0.0.1:8000/generate-dish-propositions`, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
                  'accept': 'application/json',
              },
              body: JSON.stringify(requestData),
          });

          const data = await response.json();
          this.text = data;

          this.loading = false;
      },
      getData() {
          return this.text
      },
      handleToggleClick(property) {
          this[property] = !this[property];
          console.log(this[property]);
      },
  },
  computed: {
      toggleImage() {
          return function (property) {
              return this[property] ? 'assets/img/toggleOn.svg' : 'assets/img/toggleOff.svg';
          };
      },
  },
});

const mountedApp = app.mount('#app');
