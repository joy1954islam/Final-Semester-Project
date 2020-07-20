$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-ministry .modal-content").html("");
        $("#modal-ministry").modal("show");
      },
      success: function (data) {
        $("#modal-ministry .modal-content").html(data.html_form);
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
          $("#datatable-buttons tbody").html(data.html_ministry_list);
          $("#modal-ministry").modal("hide");
        }
        else {
          $("#modal-ministry .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-ministry").click(loadForm);
  $("#modal-ministry").on("submit", ".js-ministry-create-form", saveForm);

  // Update book
  $("#datatable-buttons").on("click", ".js-update-ministry", loadForm);
  $("#modal-ministry").on("submit", ".js-ministry-update-form", saveForm);

  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-ministry", loadForm);
  $("#modal-ministry").on("submit", ".js-ministry-delete-form", saveForm);

});