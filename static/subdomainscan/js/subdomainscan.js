var table = new Vue({
    el: "#table",
    data: {
        list: []
    },
});

var form = new Vue({
    el: "#form",
    data: {
        // items: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        domainName: "",
        // pages: "",
    },
    methods: {
        // 这里判断之后，还不是qq.com这种形式，还需要将ajax传过去的domainName弄成qq.com的形式。
        isDomain: function (domain) {
            let strRegex = "^(?=^.{3,255}$)(http(s)?:\\/\\/)?(www\\.)?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+(:\\d+)*(\\/\\w+\\.\\w+)*$";
            let re = new RegExp(strRegex);
            if (re.test(domain)) {
                return true;
            } else {
                return false;
            }
        },
        getList: function () {
            let domain_flag = this.isDomain(this.domainName);
            if (domain_flag) {
                let $myModal = $('#myModal');
                $myModal.modal({backdrop: 'static'});
                table.list = [];
                this.$http.post("/subdomainscan/startsubdomainscan/", {
                    domain: this.domainName,
                    // pages: this.pages
                }, {
                    emulateJSON: true
                }).then(function (response) {
                    $myModal.modal("hide");
                    result = response.body.list;
                    table.list = result;
                });
            } else {
                this.domainName = "";
                alert("请输入正确的域名");
            }

        }
    }
});