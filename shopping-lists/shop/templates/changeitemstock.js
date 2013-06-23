<script type="text/javascript">
function checkitem(itemid) {
    $("#ref"+itemid).attr('style', "")
    //$("#"+itemid).attr('checked', true);

 $.ajax({
   url: "/changeitemstock/"+itemid,
     success: function(data){
       //chomp data
       data = data.replace(/(\n|\r)+$/, '');
       $("#ref"+itemid).attr('style', "display: none")
       if (data+'' == "True") {
           $("#txt"+itemid).attr('style', "")
       } else {
           $("#txt"+itemid).attr('style', "color: grey")
       }
   },
 });
}
</script>
