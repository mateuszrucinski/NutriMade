const app = Vue.createApp({
    data: function () {
      return {
        title: 'NutriMade',
        nutri_info_1: 'Dieta Wegańska',
        nutri_info_2: 'Dieta Wegetariańska',
        nutri_info_3: 'Bez Laktozy',
        nutri_info_4: 'Cukrzyca',
        nutri_info_4: 'Kalorie',
      }
    },
    methods: {
      async sendNutriForm() {
          // Data to be sent in the request body (if any)
          const requestData = {
            vegan_diet: true,
            vegetarian_diet: true,
            no_lactose: true,
            Diabetes: true,
            Calories: 0,
            Meal_type: "string",
            Preferences: "string"
          };

          const response = await fetch(`http://127.0.0.1:8000/generate-dish-propositions`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'accept': 'application/json',
              // You may need to include additional headers such as authentication tokens
            },
            body: JSON.stringify(requestData), // Convert the data to JSON format
            }
            );
      },
      getData() {
        return this.text
      },
    }
  }); 
  