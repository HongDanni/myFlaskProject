let name = "丹妮";
test();
function test(){
console.log("点击事件")
$.ajax({
url:"../manager/getuser",
method: "POST",
data:{
   "user" : name
},
success:function(data){
    console.log(data.data);
    render(data);
},
error:function (e){
    console.log("接口访问失败");
}
})
}
function render(data){
    let obj = data.data;
    let name = obj[0].nickname;
    console.log(name);
    $("#render_data").val(name);
    let render = document.getElementById("render_data");
    render.innerHTML = `<div>${name}<div>`;
    let table = document.createElement("ul");
    document.getElementById("body").appendChild(table);
    for(let i = 0;i<obj.length;i++){
        let nickname = obj[i].nickname;
        let password = obj[i].password;
        table.innerHTML += `<li>昵称:${nickname} 密码:${password}</li>`;
    }
}