$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-teacherEnroll .modal-content").html("");
        $("#modal-teacherEnroll").modal("show");
      },
      success: function (data) {
        $("#modal-teacherEnroll .modal-content").html(data.html_form);
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
          $("#datatable-buttons tbody").html(data.html_teacherEnroll_list);
          $("#modal-teacherEnroll").modal("hide");
        }
        else {
          $("#modal-teacherEnroll .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-teacherEnroll").click(loadForm);
  $("#modal-teacherEnroll").on("submit", ".js-teacherEnroll-create-form", saveForm);

  // Update book
  $("#datatable-buttons").on("click", ".js-update-teacherEnroll", loadForm);
  $("#modal-teacherEnroll").on("submit", ".js-teacherEnroll-update-form", saveForm);

  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-teacherEnroll", loadForm);
  $("#modal-teacherEnroll").on("submit", ".js-teacherEnroll-delete-form", saveForm);

});