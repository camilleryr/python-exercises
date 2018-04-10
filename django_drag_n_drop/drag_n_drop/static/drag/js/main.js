'use strict';

let dragula_obj = dragula([document.getElementById('left-defaults'), document.getElementById('right-defaults')]);

//query the children of the left container
let results_container = $(dragula_obj.containers[0])[0].children

dragula_obj.on('drop', e => {
    $("#issue_array")[0].value = JSON.stringify(Object.assign([], results_container).map((x, i) => {return {'id':parseInt(x.className),'priority':i}}))
})

//convert jQuery collection to array - map to convert results to a array of objects {id, priority}
let ordered_issues = Object.assign([], results_container).map((x, i) => {return {'id':parseInt(x.className),'priority':i}})

//use ajax to send backlog name and ordered_issues back to backend