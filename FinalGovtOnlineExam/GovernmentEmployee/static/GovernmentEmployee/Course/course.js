$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-course .modal-content").html("");
        $("#modal-course").modal("show");
      },
      success: function (data) {
        $("#modal-course .modal-content").html(data.html_form);
      }
    });
  };


  var saveForm = function(){
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#datatable-buttons tbody").html(data.html_course_list);
          $("#modal-course").modal("hide");
        }
        else {
          $("#modal-course .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-course").click(loadForm);
  $("#modal-course").on("submit", ".js-course-create-form", saveForm);

  // Update book
  $("#datatable-buttons").on("click", ".js-update-course", loadForm);
  $("#modal-course").on("submit", ".js-course-update-form", saveForm);

  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-course", loadForm);
  $("#modal-course").on("submit", ".js-course-delete-form", saveForm);

});