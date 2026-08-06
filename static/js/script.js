const ctx = document.getElementById('chart');

if(ctx){

new Chart(ctx,{

type:'bar',

data:{

labels:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],

datasets:[{

label:'Medicine Adherence %',

data:[90,92,87,95,91,96,94]

}]

}

});

}