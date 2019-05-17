var table = new Vue({
  el: '#table',
  data: {
    list: []
  }
});


var form = new Vue({
  el: '#form',
  data: {
    domainName: '',
    items: ['php', 'asp', 'aspx', 'jsp', 'jspx'],
    file_ext: ''
  },
  methods: {
    show: function() {
      domain = this.domainName;
      file_ext = this.file_ext;
      console.log(domain);
      console.log(file_ext);
    },

    getlist: function() {
      while(table.list.length>0){
        table.list.pop();
      }
      console.log(this.domainName);
      console.log(this.file_ext);
      this.$http.post("/dirscan/startdirscan/", {
        domainName: this.domainName,
        file_ext: this.file_ext
      }, {
        emulateJSON: true
      }).then(function(response) {
        // table.list = response.body.list
        // console.log('ajax成功: ' + response.body.list[0].url + response.body.list[0].status);
        list = response.body.list;
        for(i = 0;i<list.length;i++){
          table.list.push(list[i]);
        }
        // table.list.push(list)
      });
    }
  }
});

