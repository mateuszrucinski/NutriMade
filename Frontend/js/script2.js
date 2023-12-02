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
    //   async sendNutriForm() {
    //       // Data to be sent in the request body (if any)
    //       // Data to be sent in the request body (if any)
    //       const requestData = {
    //         vegan_diet: this.vegan_diet,
    //         vegetarian_diet: this.vegetarian_diet,
    //         no_lactose: this.no_lactose,
    //         Diabetes: this.Diabetes,
    //         Calories: this.Calories,
    //         Meal_type: this.Meal_type,
    //         Preferences: this.Preferences,
    //     };

    //       this.loading = true;

    //       // method post
    //       const response = await fetch(`http://127.0.0.1:8000/generate-dish-propositions`, {
    //         method: 'POST',
    //         headers: {
    //           'Content-Type': 'application/json',
    //           'accept': 'application/json',
    //           // You may need to include additional headers such as authentication tokens
    //         },
    //         body: JSON.stringify(requestData), // Convert the data to JSON format
    //         }
    //         );

      
    //         this.loading = false;

    //         window.location.href = 'propozycja.html';
    //   },
      getData() {
        return this.text
      },
      // Method to handle toggle clicks
      handleToggleClick(property) {
        this[property] = !this[property];
        console.log(this[property]);
      },
      async executeGetMethod() {
        const response = await fetch(`http://127.0.0.1:8000/generate-dish-propositions/sending-with-get-method`);
        response.json();
      }
    },
    mounted() {
        // Call the method when the component is mounted
        this.executeGetMethod();
    },
  }); 
  