var vm = new Vue({
  el: '#form',
  data: {
    domainName: '',
  },
  methods: {
    cms_getlist: function() {
      this.$http.post('/cmsdistinguish/startcmsdistinguish', {
        url: this.domainName
      }, {
        emulateJSON: true
      }).then(function(response){
          console.log(response.body.list[0].cms);
      });
    }
  }
});
