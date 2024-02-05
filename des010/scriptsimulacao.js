


    

/*
var info1 = 20
var info2 = 50
var info3 = 30

*/

/*
var checkboxinfo1 = window.document.querySelector("#info1");


function enviar() {
    if (checkboxinfo1.checked) {var info1=Number(20)}
    else { var info2=Number(50)}
    var total = Number(info1)+Number(info2)
    var total2 = String(total)
    return info38.innerHTML= `Total: R$ ${total2}.`
};

PARA MOSTRAR ARRAY NO DOCUMENTO

function enviar() {
    let html = '';
    for (var n = 0; n<=10; n++) {
        if (n == 5) 
            {html+= '<p>' + (`Deu certo: ${n}`)} 
            else 
                {html+= '<p>'+ (`Deu certo tbm: ${n}`)}
       
    }
    document.querySelector('#info38').innerHTML=html
    
}

*/


function enviar() {
    var checkboxinfo0 = window.document.querySelector("#info1");
    var checkboxinfo1 = window.document.querySelector("#info2");
    var checkboxinfo2 = window.document.querySelector("#info3");
    var checkboxinfo3 = window.document.querySelector("#info4");
    var checkboxinfo4 = window.document.querySelector("#info5");
    var checkboxinfo5 = window.document.querySelector("#info6");
    var checkboxinfo6 = window.document.querySelector("#info10");
    var checkboxinfo7 = window.document.querySelector("#info11");
    var checkboxinfo8 = window.document.querySelector("#info12");
    var checkboxinfo9 = window.document.querySelector("#info13");
    var checkboxinfo10 = window.document.querySelector("#info14");
    var checkboxinfo11 = window.document.querySelector("#info15");
    var checkboxinfo12 = window.document.querySelector("#info16");
    var checkboxinfo13 = window.document.querySelector("#info17");
    var checkboxinfo14 = window.document.querySelector("#info18");
    var checkboxinfo15 = window.document.querySelector("#info19");
    var checkboxinfo16 = window.document.querySelector("#info20");
    var checkboxinfo17 = window.document.querySelector("#info21");
    var checkboxinfo18 = window.document.querySelector("#info22");
    var checkboxinfo19 = window.document.querySelector("#info23");
    var checkboxinfo20 = window.document.querySelector("#info24");
    var checkboxinfo21 = window.document.querySelector("#info25");
    var checkboxinfo22 = window.document.querySelector("#info26");
    var checkboxinfo23 = window.document.querySelector("#info27");
    var checkboxinfo24 = window.document.querySelector("#info28");
    var checkboxinfo25 = window.document.querySelector("#info29");
    var checkboxinfo26 = window.document.querySelector("#info30");
    var checkboxinfo27 = window.document.querySelector("#info31");
    var checkboxinfo28 = window.document.querySelector("#info32");
    var checkboxinfo29 = window.document.querySelector("#info33");
    var checkboxinfo30 = window.document.querySelector("#info34");
    var checkboxinfo31 = window.document.querySelector("#info35");
    var checkboxinfo32 = window.document.querySelector("#info36");
    var checkboxinfo33 = window.document.querySelector("#info37");

    let caminho=[checkboxinfo0,checkboxinfo1, checkboxinfo2, checkboxinfo3, checkboxinfo4, checkboxinfo5, checkboxinfo6, checkboxinfo7, checkboxinfo8, checkboxinfo9, checkboxinfo10, checkboxinfo11, checkboxinfo12, checkboxinfo13, checkboxinfo14, checkboxinfo15, checkboxinfo16, checkboxinfo17, checkboxinfo18, checkboxinfo19, checkboxinfo20, checkboxinfo21, checkboxinfo22, checkboxinfo23, checkboxinfo24, checkboxinfo25, checkboxinfo26, checkboxinfo27, checkboxinfo28, checkboxinfo29, checkboxinfo30, checkboxinfo31, checkboxinfo32, checkboxinfo33]

    var info = window.document.getElementById("info38");
    let valor = [20, 50, 20, 0, 50, 0, 20, 50, 50, 50, 100, 50, 20, 50, 50, 100, 50, 50, 50, 50, 50, 50, 20, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 0]
    
    var teste = 0

    let resultado = []

    var total = 0
    
    let html = '';

    for (var n = 0; n<34; n++) {
        if (caminho[n].checked) 
            {total = total + valor[n]}  
           
        
    }
    document.querySelector('#info38').innerHTML=total
    
}








