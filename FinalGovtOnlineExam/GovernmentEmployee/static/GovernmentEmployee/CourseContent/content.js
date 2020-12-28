$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-topic .modal-content").html("");
        $("#modal-topic").modal("show");
      },
      success: function (data) {
        $("#modal-topic .modal-content").html(data.html_form);
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
          $("#datatable-buttons tbody").html(data.html_topic_list);
          $("#modal-topic").modal("hide");
        }
        else {
          $("#modal-topic .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create
  $(".js-create-topic").click(loadForm);
  $("#modal-topic").on("submit", ".js-topic-create-form", saveForm);

  // Update
  $("#datatable-buttons").on("click", ".js-update-topic", loadForm);
  $("#modal-topic").on("submit", ".js-topic-update-form", saveForm);

  // Delete
  $("#datatable-buttons").on("click", ".js-delete-topic", loadForm);
  $("#modal-topic").on("submit", ".js-topic-delete-form", saveForm);

    //view
  $("#datatable-buttons").on("click", ".js-view-topic", loadForm);
  $("#modal-topic").on("submit", ".js-topic-view-form", saveForm);

});