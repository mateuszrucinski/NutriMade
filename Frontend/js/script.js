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
      async getFacts() {
          const response = await fetch(`http://127.0.0.1:8000/catfact/${this.number}`);
          
          if (response.ok) {
            const data = await response.json();
            this.text = data;
            
            // Data was sent successfully, navigate to another page
            window.location.href = 'frontNext.html';
          } else {
            // Handle error cases if needed
            console.error('Backend request failed');
          }
      },
      getData() {
        return this.text
      },
    }
  }); 
  