$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-lecture .modal-content").html("");
        $("#modal-lecture").modal("show");
      },
      success: function (data) {
        $("#modal-lecture .modal-content").html(data.html_form);
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
          $("#datatable-buttons tbody").html(data.html_lecture_list);
          $("#modal-lecture").modal("hide");
        }
        else {
          $("#modal-lecture .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-lecture").click(loadForm);
  $("#modal-lecture").on("submit", ".js-lecture-create-form", saveForm);

  // Update book
  $("#datatable-buttons").on("click", ".js-update-lecture", loadForm);
  $("#modal-lecture").on("submit", ".js-lecture-update-form", saveForm);

  // Delete book
  $("#datatable-buttons").on("click", ".js-delete-lecture", loadForm);
  $("#modal-lecture").on("submit", ".js-lecture-delete-form", saveForm);

});