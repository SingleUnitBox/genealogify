$("#deleteLicense").on("show.bs.modal", function (event) {
  var button = $(event.relatedTarget); // Button that triggered the modal
  var pk = button.data("license-pk"); // Extract info from data-* attributes
  var title = button.data("license-title"); // Extract info from data-* attributes
  var modal = $(this);
  modal.find(".modal-title").text("Delete #" + pk);
  modal.find("#delete_link").attr("href", "/licenses/delete/" + pk);
  modal
    .find(".modal-body")
    .html(
      `Are you sure to delete license?: <br><br><b>${title}</b>` +
        "<br>" +
        "<br>All docs will be deleted. <br><br>" +
        '<span class="text text-danger">Are you sure? </span>'
    );
});