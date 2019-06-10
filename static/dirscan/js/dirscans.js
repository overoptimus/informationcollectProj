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
        file_ext: '',
        file_ext_flag: ""
    },
    methods: {
        show: function () {
            let domain = this.domainName;
            let file_ext = this.file_ext;
            console.log(domain);
            console.log(file_ext);
        },
        isFile_ext: function (file_ext) {
            if (file_ext !== "") {
                return true;
            } else {
                return false;
            }
        },
        isDomain: function (domain) {
            let strRegex = "^(?=^.{3,255}$)(http(s)?:\\/\\/)?(www\\.)?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+(:\\d+)*(\\/\\w+\\.\\w+)*$";
            let re = new RegExp(strRegex);
            if (re.test(domain)) {
                return true;
            } else {
                return false;
            }
        },
        getlist: function () {
            let domain_flag = this.isDomain(this.domainName);
            let file_flag = this.isFile_ext(this.file_ext);
            let flag = false;
            if (!file_flag) {
                this.file_ext_flag = "请选择文件类型！";
                console.log("没文件类型");
            } else {
                // let $file_ext_flag = $('#file_ext_flag');
                console.log("有文件类型");
                this.file_ext_flag = "";
            }
            if (domain_flag && file_flag) {
                flag = true;
            }
            if (flag) {
                let $myModal = $('#myModal');
                $myModal.modal({backdrop: 'static'});
                while (table.list.length > 0) {
                    table.list.pop();
                }
                console.log(this.domainName);
                console.log(this.file_ext);
                this.$http.post("/dirscan/startdirscan/", {
                    domainName: this.domainName,
                    file_ext: this.file_ext
                }, {
                    emulateJSON: true
                }).then(function (response) {
                    $myModal.modal("hide");
                    // table.list = response.body.list
                    // console.log('ajax成功: ' + response.body.list[0].url + response.body.list[0].status);
                    let list = response.body.list;
                    for (i = 0; i < list.length; i++) {
                        table.list.push(list[i]);
                    }
                    // table.list.push(list)
                });
            } else {
                if (!domain_flag) {
                    if (this.domainName === "") {
                        alert("请输入域名！");
                    } else {
                        this.domainName = "";
                        alert("请输入正确的域名！");
                    }
                }
                if (!file_flag) {
                    this.file_ext_flag = "请选择文件类型";
                }
            }

        }
    }
});

