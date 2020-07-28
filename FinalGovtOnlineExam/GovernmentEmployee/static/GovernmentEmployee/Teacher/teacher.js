$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-teacher .modal-content").html("");
        $("#modal-teacher").modal("show");
      },
      success: function (data) {
        $("#modal-teacher .modal-content").html(data.html_form);
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
          $("#datatable-buttons tbody").html(data.html_teacher_list);
          $("#modal-teacher").modal("hide");
        }
        else {
          $("#modal-teacher .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create teacher
  $(".js-create-teacher").click(loadForm);
  $("#modal-teacher").on("submit", ".js-teacher-create-form", saveForm);

  // Update teacher
  $("#datatable-buttons").on("click", ".js-update-teacher", loadForm);
  $("#modal-teacher").on("submit", ".js-teacher-update-form", saveForm);

  // Delete teacher
  $("#datatable-buttons").on("click", ".js-delete-teacher", loadForm);
  $("#modal-teacher").on("submit", ".js-teacher-delete-form", saveForm);

  // view teacher
  $("#datatable-buttons").on("click", ".js-view-teacher", loadForm);
  $("#modal-teacher").on("submit", ".js-teacher-view-form", saveForm);

});