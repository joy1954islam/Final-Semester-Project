$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-govtemployee .modal-content").html("");
        $("#modal-govtemployee").modal("show");
      },
      success: function (data) {
        $("#modal-govtemployee .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#datatable-buttons tbody").html(data.html_govtemployee_list);
          $("#modal-govtemployee").modal("hide");
        }
        else {
          $("#modal-govtemployee .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-govtemployee").click(loadForm);
  $("#modal-govtemployee").on("submit", ".js-govtemployee-create-form", saveForm);

  // Update book
  $("#datatable-buttons").on("click", ".js-update-govtemployee", loadForm);
  $("#modal-govtemployee").on("submit", ".js-govtemployee-update-form", saveForm);

  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-govtemployee", loadForm);
  $("#modal-govtemployee").on("submit", ".js-govtemployee-delete-form", saveForm);

});