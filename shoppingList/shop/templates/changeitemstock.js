<script type="text/javascript">
function checkitem(itemid) {
    // spiner
    $("#ref"+itemid).attr('style', "");
    // Checkbox
    $("#"+itemid).attr("disabled", true);

 $.ajax({
   url: "/changeitemstock/"+itemid,
     success: function(data){
      // spiner
       $("#ref"+itemid).attr('style', "display: none")
      // Checkbox
      $("#"+itemid).removeAttr("disabled");

       // Text
       //chomp data
       // data = data.replace(/(\n|\r)+$/, '');
       // if (data+'' == "True") {
       //     $("#txt"+itemid).attr('style', "")
       // } else {
       //     $("#txt"+itemid).attr('style', "color: grey")
       // }
   },
 });
}
</script>
