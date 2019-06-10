var table = new Vue({
    el: "#table",
    data: {
        "result": []
    }
});


var form = new Vue({
    el: "#form",
    data: {
        "domainName": "",
        "port_Range": "",
        "message": ""
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
        isPortrange: function (port_range) {
            if (port_range === "") {
                return true;
            } else {

                let strRegex = "(([0-9]|[1-9]\d|[1-9]\d{2}|[1-9]\d{3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])-([0-9]|[1-9]d|[1-9]d{2}|[1-9]d{3}|[1-5]d{4}|6[0-4]d{3}|65[0-4]d{2}|655[0-2]d|6553[0-5]))(,([0-9]|[1-9]d|[1-9]d{2}|[1-9]d{3}|[1-5]d{4}|6[0-4]d{3}|65[0-4]d{2}|655[0-2]d|6553[0-5]))*";
                let re = new RegExp(strRegex);
                if (re.test(port_range)) {
                    let port_range_1 = port_range.split(",")[0];
                    let port_range_min = port_range_1.split("-")[0];
                    let port_range_max = port_range_1.split("-")[1];
                    if (port_range_min < port_range_max) {
                        return true;
                    } else {
                        console.log("第一个re");
                        return false;
                    }
                } else {
                    let strRegex = "(([0-9]|[1-9]d|[1-9]d{2}|[1-9]d{3}|[1-5]d{4}|6[0-4]d{3}|65[0-4]d{2}|655[0-2]d|6553[0-5]),)*?([0-9]|[1-9]d|[1-9]d{2}|[1-9]d{3}|[1-5]d{4}|6[0-4]d{3}|65[0-4]d{2}|655[0-2]d|6553[0-5])";
                    let re = new RegExp(strRegex);
                    if (re.test(port_range)) {
                        return true;
                    } else {
                        console.log("第二个re");
                        return false;

                    }
                }
            }
        },
        get_result: function () {
            let domain_flag = this.isDomain(this.domainName);
            let port_range_flag = this.isPortrange(this.port_Range);
            let flag = false;
            if (domain_flag && port_range_flag) {
                flag = true;
            }
            if (flag) {
                this.message = "";
                let portRange;
                let $myModal = $('#myModal');
                $myModal.modal({backdrop: 'static'});
                if (this.port_Range === "") {
                    portRange = "1-1024";
                } else {
                    portRange = this.port_Range;
                }
                while (table.result.length > 0) {
                    table.result.pop();
                }
                console.log(this.domainName);
                this.$http.post('/portscan/startportscan/', {
                    domainName: this.domainName,
                    port_range: portRange,
                }, {
                    emulateJSON: true
                }).then(function (response) {
                    $myModal.modal("hide");
                    result = response.body.result;
                    for (let i = 0; i < result.length; i++) {
                        table.result.push(result[i]);
                    }

                });
            } else {
                if (!domain_flag) {
                    this.domainName = "";
                    alert("请输入正确的域名");
                }
                if (!port_range_flag) {
                    this.message = "请严格按照提示输入端口范围";
                }

            }

        }
    }
});
