'use strict';

let dragula_obj = dragula([document.getElementById('left-defaults'), document.getElementById('right-defaults')]);

//query the children of the left container
let results_container = $(drake.containers[0])[0].children

//convert jQuery collection to array - map to convert results to a array of objects {id, priority}
let ordered_issues = Object.assign([], array).map((x, i) => {return {'id':parseInt(x.className),'priority':i}})

//use ajax to send backlog name and ordered_issues back to backend