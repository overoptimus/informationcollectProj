var table = new Vue({
  el: '#table',
  data: {
    list: '',
    i: 0,
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
      console.log(this.domainName);
      console.log(this.file_ext);
      this.$http.post("/dirscan/startdirscan/", {
        domainName: this.domainName,
        file_ext: this.file_ext
      }, {
        emulateJSON: true
      }).then(function(response) {
        table.list = response.body.list
        console.log('ajax成功: ' + response.body.list[0].url + response.body.list[0].status);
      });
    }
  }
});



// new Vue({
//     el: '#test',
//     data: {
//       message: 'test'
//     }
//   })



// {'file_ext':
// {'file_ext':
// {'file_ext':
// {'file_ext':
// {'file_ext':
//
//
// }
// }
// }
// }
// }
