function DeleteRowFunction() {
    // event.target will be the input element.
    var td = event.target.parentNode;
    var tr = td.parentNode; // the row to be removed
    tr.parentNode.removeChild(tr);
}



function add_row() {
    const t_body = document.querySelector("#t_body");

    const tr = document.createElement('tr');

    const td1 = document.createElement('td')
    const td2 = document.createElement('td')
    const td3 = document.createElement('td')
    const td4 = document.createElement('td')

    // <input type="number" name="value" class="form-control" required="">
    // <input type="number" name="num_sell" class="form-control" required="">



    const num_sell_input = document.createElement('input')
    num_sell_input.setAttribute('type', 'number')
    num_sell_input.setAttribute('name', 'num_sell')
    num_sell_input.setAttribute('required', '')
    num_sell_input.classList.add('form-control')


    const value_input = document.createElement('input')
    value_input.setAttribute('type', 'number')
    value_input.setAttribute('name', 'value')
    value_input.setAttribute('required', '')
    value_input.classList.add('form-control')


    const select_element = `
<select name="draw_time" class="form-control" required="">
  <option value="" selected="">---------</option>
  <option value="8:30">Early Bird</option>
  <option value="10:30">Drive Time</option>
  <option value="1:00">Midday</option>
  <option value="3:00">Afternoon</option>
  <option value="5:00">Evening</option>
  <option value="8:25">Late Night</option>
</select>
`

    const remove_btn = `
    <input type="button" value="×" onclick="DeleteRowFunction()" class="btn btn-danger">
    `




    td1.appendChild(num_sell_input)
    td2.appendChild(value_input)

    td4.innerHTML = remove_btn

    tr.appendChild(td1)
    tr.appendChild(td2)

    tr.appendChild(td4)




    t_body.appendChild(tr)
}

