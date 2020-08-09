$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-employee .modal-content").html("");
        $("#modal-employee").modal("show");
      },
      success: function (data) {
        $("#modal-employee .modal-content").html(data.html_form);
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
          $("#datatable-buttons tbody").html(data.html_employee_list);
          $("#modal-employee").modal("hide");
        }
        else {
          $("#modal-employee .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create teacher
  $(".js-create-employee").click(loadForm);
  $("#modal-employee").on("submit", ".js-employee-create-form", saveForm);

  // Update teacher
  $("#datatable-buttons").on("click", ".js-update-employee", loadForm);
  $("#modal-employee").on("submit", ".js-employee-update-form", saveForm);

  // Delete teacher
  $("#datatable-buttons").on("click", ".js-delete-employee", loadForm);
  $("#modal-employee").on("submit", ".js-employee-delete-form", saveForm);

  // view teacher
  $("#datatable-buttons").on("click", ".js-view-employee", loadForm);
  $("#modal-employee").on("submit", ".js-employee-view-form", saveForm);

});