$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-studentEnroll .modal-content").html("");
        $("#modal-studentEnroll").modal("show");
      },
      success: function (data) {
        $("#modal-studentEnroll .modal-content").html(data.html_form);
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
          $("#datatable-buttons tbody").html(data.html_studentEnroll_list);
          $("#modal-studentEnroll").modal("hide");
        }
        else {
          $("#modal-studentEnroll .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-studentEnroll").click(loadForm);
  $("#modal-studentEnroll").on("submit", ".js-studentEnroll-create-form", saveForm);

  // Update book
  $("#datatable-buttons").on("click", ".js-update-studentEnroll", loadForm);
  $("#modal-studentEnroll").on("submit", ".js-studentEnroll-update-form", saveForm);

  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-studentEnroll", loadForm);
  $("#modal-studentEnroll").on("submit", ".js-studentEnroll-delete-form", saveForm);

});