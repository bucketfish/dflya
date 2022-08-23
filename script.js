var selected_filters = []


function arrayRemove(arr, value) {

    return arr.filter(function(ele){
        return ele != value;
    });
}

function search() {
  // Declare variables
  // var input, filter, resources, a, i, txtValue;
  var input = document.getElementById('search-bar');
  var filter = input.value.toUpperCase();
  var resources = document.getElementsByClassName("resource-box");


  // Loop through all list items, and hide those who don't match the search query
  for (var i = 0; i < resources.length; i++) {
    var current = resources[i];
    var title = resources[i].getElementsByTagName("h1")[0];
    var txtValue = title.textContent || title.innerText;

    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      current.style.display = "";
    } else {
      current.style.display = "none";
    }
  }
}


function filter(filtername){

  var filter = filtername.toUpperCase();

  if (selected_filters.includes(filter)){
    selected_filters = arrayRemove(selected_filters, filter)
    document.getElementById(filtername).dataset.selected = 0;
  }
  else {
    selected_filters.push(filter)
    document.getElementById(filtername).dataset.selected = 1;
  }

  var resources = document.getElementsByClassName("resource-box");

  // Loop through all list items, and hide those who don't match the search query
  for (var i = 0; i < resources.length; i++) {
    var current = resources[i];
    var tags = resources[i].getElementsByClassName("tags-list")[0];
    var txtValue = tags.textContent || tags.innerText;
    var show = true;

    for (var j = 0; j < selected_filters.length; j++){
      if (txtValue.toUpperCase().indexOf(selected_filters[j]) <= -1) {
        show = false;
      }
    }
    if (show){
      current.style.display = "";
    }
    else {
      current.style.display = "none";
    }

  }
}
