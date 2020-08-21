$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-student .modal-content").html("");
        $("#modal-student").modal("show");
      },
      success: function (data) {
        $("#modal-student .modal-content").html(data.html_form);
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
          $("#datatable-buttons tbody").html(data.html_student_list);
          $("#modal-student").modal("hide");
        }
        else {
          $("#modal-student .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-student").click(loadForm);
  $("#modal-student").on("submit", ".js-student-create-form", saveForm);

  // Update book
  $("#datatable-buttons").on("click", ".js-update-student", loadForm);
  $("#modal-student").on("submit", ".js-ministry-update-form", saveForm);

  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-student", loadForm);
  $("#modal-student").on("submit", ".js-student-delete-form", saveForm);

});