var result = new Vue({
    el: "#cmsresult",
    data: {
        cmsType: "",
        hasResult: 0,
    },
    methods: {
        changeStatus: function () {
            if (this.cmsType !== "") {
                this.hasResult = 1;
            } else {
                this.hasResult = 0;
            }
        }
    }
});

var input = new Vue({
    el: '#form',
    data: {
        domainName: '',
    },
    methods: {
        isDomain: function (domain) {
            let strRegex = "^(?=^.{3,255}$)(http(s)?:\\/\\/)?(www\\.)?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+(:\\d+)*(\\/\\w+\\.\\w+)*$";
            let re = new RegExp(strRegex);
            if (re.test(domain)) {
                return true;
            } else {
                return false;
            }
        },
        cms_getlist: function () {
            let domain_flag = this.isDomain(this.domainName);
            if (domain_flag) {
                let $myModal = $('#myModal');
                $myModal.modal({backdrop: 'static'});
                result.cmsType = "";
                result.changeStatus();
                this.$http.post('/cmsdistinguish/startcmsdistinguish/', {
                    url: this.domainName
                }, {
                    emulateJSON: true
                }).then(function (response) {
                    // $myModal.attr("style", "display:none");
                    $myModal.modal("hide");
                    // console.log(response.body.list[0].cms);
                    result.cmsType = response.body.list[0].cms;
                    result.changeStatus();
                });
            } else {
                if (this.domainName === "") {
                    alert("请输入域名！");
                } else {
                    this.domainName = "";
                    alert("请输入正确的域名！");
                }
            }

        }
    }
});


