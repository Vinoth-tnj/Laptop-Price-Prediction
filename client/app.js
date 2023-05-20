function getRAMValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var ss = document.getElementById("uiScreenSize");
  var rams = getRAMValue();
  var manufacturer = document.getElementById("uimanufacturer");
  var Category = document.getElementById("uiCategory");
  var Screen = document.getElementById("uiScreen");
  var CPU = document.getElementById("uiCPU");
  var Storage = document.getElementById("uiStorage");
  var GPU = document.getElementById("uiGPU");
  var estPrice = document.getElementById("uiEstimatedPrice");

   var url = "http://127.0.0.1:8000/"; //Use this if you are NOT using nginx which is first 7 tutorials
  // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      total_ss: parseFloat(ss.value),
      ram: rams,
      manufacturer: manufacturer.value,
      Category: Category.value,
      Screen: Screen.value,
      CPU: CPU.value,
      Storage: Storage.value,
      GPU: GPU.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>Rs." + data.estimated_price.toString() + "</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:8000/"; // Use this if you are NOT using nginx which is first 7 tutorials
  // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var manufacturer = data.manufacturers;
          var category = data.categorys;
          var screen = data.screens;
          var cpu = data.cpus;
          var storage = data.storages;
          var gpu = data.gpus;
          var uiLocations = document.getElementById("uiLocations");
          $('#uimanufacturer').empty();
          $('#uiCategory').empty();
          $('#uiScreen').empty();
          $('#uiCPU').empty();
          $('#uiStorage').empty();
          $('#uiGPU').empty();
          for(var i in manufacturer) {
            var opt = new Option(manufacturer[i]);
            $('#uimanufacturer').append(opt);
        }
          for(var i in category) {
            var opt = new Option(category[i]);
            $('#uiCategory').append(opt);
        }
          for(var i in screen) {
            var opt = new Option(screen[i]);
            $('#uiScreen').append(opt);
        }
          for(var i in cpu) {
            var opt = new Option(cpu[i]);
            $('#uiCPU').append(opt);
        }
          for(var i in storage) {
            var opt = new Option(storage[i]);
            $('#uiStorage').append(opt);
        }
          for(var i in gpu) {
              var opt = new Option(gpu[i]);
              $('#uiGPU').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
