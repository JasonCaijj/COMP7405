$(document).ready(function(){
  // bs 
  $("#btn_bs_cal").click(function(){
    //asset value
    var s
    if ($("#bs_s").val()==""){
      alert("Please input asset value");
      return
    }else{
      s = $("#bs_s").val();
      //alert("Value: " +s);
    }

    //volatility
    var vol
    if ($("#bs_vol").val()==""){
      alert("Please input volatility");
      return
    }else{
      vol = $("#bs_vol").val();
      //alert("Value: " +vol);
    }

    //strike price
    var k
    if ($("#bs_k").val()==""){
      alert("Please input strike price");
      return
    }else{
      k = $("#bs_k").val();
      //alert("Value: " +k);
    }

    //risk-free rate
    var r
    if ($("#bs_r").val()==""){
      alert("Please input risk-free rate");
      return
    }else{
      r = $("#bs_r").val();
      //alert("Value: " +r);
    }

    //time to maturity
    var t
    if ($("#bs_t").val()==""){
      alert("Please input time to maturity");
      return
    }else{
      t = $("#bs_t").val();
      //alert("Value: " +t);
    }

    //type
    var type
    if ($("#bs_type").val()==""){
      alert("Please input option type");
      return
    }else{
      type = $("#bs_type").val();
      //alert("Value: " +type);
    }

    alert("begin to post data")

    $.post("/bs",
      {
        bs_s: s,
        bs_vol: vol,
        bs_k: k,
        bs_r: r,
        bs_t: t,
        bs_type: type
      },

      function(data,status){
        //alert("Data: "+data+'\nStatus: '+status);
        $("#BS_value").text(data);
      });
    
    $("#BS_value").text('Calculating...');

      



    


  });

  //imp
  $("#btn_imp_cal").click(function(){
    //asset value
    var s
    if ($("#imp_S").val()==""){
      alert("Please input asset value");
      return
    }else{
      s = $("#imp_S").val();
      //alert("Value: " +s);
    }

    //repo rate
    var q
    if ($("#imp_q").val()==""){
      alert("Please input repo rate");
      return
    }else{
      q = $("#imp_q").val();
      //alert("Value: " +vol);
    }

    //option_value
    var value
    if ($("#imp_value").val()==""){
      alert("Please input option value");
      return
    }else{
      value = $("#imp_value").val();
      //alert("Value: " +vol);
    }

    //strike price
    var k
    if ($("#imp_K").val()==""){
      alert("Please input strike price");
      return
    }else{
      k = $("#imp_K").val();
      //alert("Value: " +k);
    }

    //risk-free rate
    var r
    if ($("#imp_r").val()==""){
      alert("Please input risk-free rate");
      return
    }else{
      r = $("#imp_r").val();
      //alert("Value: " +r);
    }

    //time to maturity
    var t
    if ($("#imp_t").val()==""){
      alert("Please input time to maturity");
      return
    }else{
      t = $("#imp_t").val();
      //alert("Value: " +t);
    }

    //type
    var type
    if ($("#imp_type").val()==""){
      alert("Please input option type");
      return
    }else{
      type = $("#imp_type").val();
      //alert("Value: " +type);
    }

    alert("begin to post data")

    $.post("/imp",
      {
        imp_s: s,
        imp_q: q,
        imp_value: value,
        imp_k: k,
        imp_r: r,
        imp_t: t,
        imp_type: type
      },

      function(data,status){
        //alert("Data: "+data+'\nStatus: '+status);
        $("#imp_ans").text(data);
      });
    
    $("#imp_ans").text('Calculating...');

      



    


  });

  $("#btn_cfs_cal").click(function(){
    //asset value
    var s
    if ($("#cfs_S").val()==""){
      alert("Please input asset value");
      return
    }else{
      s = $("#cfs_S").val();
      //alert("Value: " +s);
    }

    //volatility
    var vol
    if ($("#cfs_vol").val()==""){
      alert("Please input volatility");
      return
    }else{
      vol = $("#cfs_vol").val();
      //alert("Value: " +vol);
    }

    //strike price
    var N
    if ($("#cfs_N").val()==""){
      alert("Please input n");
      return
    }else{
      N = $("#cfs_N").val();
      //alert("Value: " +k);
    }

    //strike price
    var k
    if ($("#cfs_K").val()==""){
      alert("Please input strike price");
      return
    }else{
      k = $("#cfs_K").val();
      //alert("Value: " +k);
    }

    //risk-free rate
    var r
    if ($("#cfs_r").val()==""){
      alert("Please input risk-free rate");
      return
    }else{
      r = $("#cfs_r").val();
      //alert("Value: " +r);
    }

    //time to maturity
    var t
    if ($("#cfs_t").val()==""){
      alert("Please input time to maturity");
      return
    }else{
      t = $("#cfs_t").val();
      //alert("Value: " +t);
    }

    //type
    var type
    if ($("#cfs_type").val()==""){
      alert("Please input option type");
      return
    }else{
      type = $("#cfs_type").val();
      //alert("Value: " +type);
    }

    alert("begin to post data")

    $.post("/cfs",
      {
        cfs_s: s,
        cfs_vol: vol,
        cfs_N: N,
        cfs_k: k,
        cfs_r: r,
        cfs_t: t,
        cfs_type: type
      },

      function(data,status){
        //alert("Data: "+data+'\nStatus: '+status);
        $("#cfs_ans").text(data);
      });
    
    $("#cfs_ans").text('Calculating...');

      



    


  });

  $("#btn_cfb_cal").click(function(){
    //asset value 1
    var s1
    if ($("#cfb_s1").val()==""){
      alert("Please input asset value 1");
      return
    }else{
      s1 = $("#cfb_s1").val();
      //alert("Value: " +s);
    }

     //asset value 2
     var s2
     if ($("#cfb_s2").val()==""){
       alert("Please input asset value 2");
       return
     }else{
       s2 = $("#cfb_s2").val();
       //alert("Value: " +s);
     }

    //volatility
    var vol1
    if ($("#cfb_vol1").val()==""){
      alert("Please input volatility 1");
      return
    }else{
      vol1 = $("#cfb_vol1").val();
      //alert("Value: " +vol);
    }

    var vol2
    if ($("#cfb_vol2").val()==""){
      alert("Please input volatility 2");
      return
    }else{
      vol2 = $("#cfb_vol2").val();
      //alert("Value: " +vol);
    }

    //strike price
    var k
    if ($("#cfb_k").val()==""){
      alert("Please input strike price");
      return
    }else{
      k = $("#cfb_k").val();
      //alert("Value: " +k);
    }

    //risk-free rate
    var r
    if ($("#cfb_r").val()==""){
      alert("Please input risk-free rate");
      return
    }else{
      r = $("#cfb_r").val();
      //alert("Value: " +r);
    }

    //time to maturity
    var t
    if ($("#cfb_t").val()==""){
      alert("Please input time to maturity");
      return
    }else{
      t = $("#cfb_t").val();
      //alert("Value: " +t);
    }

    //type
    var type
    if ($("#cfb_type").val()==""){
      alert("Please input option type");
      return
    }else{
      type = $("#cfb_type").val();
      //alert("Value: " +type);
    }

    var rho
    if ($("#cfb_rho").val()==""){
      alert("Please input rho");
      return
    }else{
      rho = $("#cfb_rho").val();
      //alert("Value: " +type);
    }

    alert("begin to post data")

    $.post("/cfb",
      {
        cfb_s1: s1,
        cfb_s2: s2,
        cfb_vol1: vol1,
        cfb_vol2: vol2,
        cfb_k: k,
        cfb_r: r,
        cfb_t: t,
        cfb_rho: rho,
        cfb_type: type
      },

      function(data,status){
        //alert("Data: "+data+'\nStatus: '+status);
        $("#cfb_ans").text(data);
      });
    
    $("#cfb_ans").text('Calculating...');

      



    


  });

  $("#btn_mca_cal").click(function(){
    //asset value
    var s
    if ($("#mca_S").val()==""){
      alert("Please input asset value");
      return
    }else{
      s = $("#mca_S").val();
      //alert("Value: " +s);
    }

    //volatility
    var vol
    if ($("#mca_vol").val()==""){
      alert("Please input volatility");
      return
    }else{
      vol = $("#mca_vol").val();
      //alert("Value: " +vol);
    }

    //strike price
    var N
    if ($("#mca_N").val()==""){
      alert("Please input n");
      return
    }else{
      N = $("#mca_N").val();
      //alert("Value: " +k);
    }

    //strike price
    var k
    if ($("#mca_K").val()==""){
      alert("Please input strike price");
      return
    }else{
      k = $("#mca_K").val();
      //alert("Value: " +k);
    }

    //risk-free rate
    var r
    if ($("#mca_r").val()==""){
      alert("Please input risk-free rate");
      return
    }else{
      r = $("#mca_r").val();
      //alert("Value: " +r);
    }

    //time to maturity
    var t
    if ($("#mca_t").val()==""){
      alert("Please input time to maturity");
      return
    }else{
      t = $("#mca_t").val();
      //alert("Value: " +t);
    }

    //I
    var I
    if ($("#mca_I").val()==""){
      alert("Please input Num of Paths");
      return
    }else{
      I = $("#mca_I").val();
      //alert("Value: " +t);
    }

    //type
    var type
    if ($("#mca_type").val()==""){
      alert("Please input option type");
      return
    }else{
      type = $("#mca_type").val();
      //alert("Value: " +type);
    }

    var c_v
    if ($("#mca_c_v").val()==""){
      alert("Please input Control Variate");
      return
    }else{
      c_v = $("#mca_c_v").val();
      //alert("Value: " +type);
    }

    alert("begin to post data")

    $.post("/mca",
      {
        mca_s: s,
        mca_vol: vol,
        mca_N: N,
        mca_k: k,
        mca_r: r,
        mca_t: t,
        mca_I: I,
        mca_c_v: c_v,
        mca_type: type
      },

      function(data,status){
        //alert("Data: "+data+'\nStatus: '+status);
        $("#mca_ans").text(data);
      });
    
    $("#mca_ans").text('Calculating...');

      



    


  });

  $("#btn_mcb_cal").click(function(){
    //asset value 1
    var s1
    if ($("#mcb_s1").val()==""){
      alert("Please input asset value 1");
      return
    }else{
      s1 = $("#mcb_s1").val();
      //alert("Value: " +s);  
    }

     //asset value 2
     var s2
     if ($("#mcb_s2").val()==""){
       alert("Please input asset value 2");
       return
     }else{
       s2 = $("#mcb_s2").val();
       //alert("Value: " +s);
     }

    //volatility
    var vol1
    if ($("#mcb_vol1").val()==""){
      alert("Please input volatility 1");
      return
    }else{
      vol1 = $("#mcb_vol1").val();
      //alert("Value: " +vol);
    }

    var vol2
    if ($("#mcb_vol2").val()==""){
      alert("Please input volatility 2");
      return
    }else{
      vol2 = $("#mcb_vol2").val();
      //alert("Value: " +vol);
    }

    var I
    if ($("#mcb_I").val()==""){
      alert("Please input Num of Paths");
      return
    }else{
      I = $("#mcb_I").val();
      //alert("Value: " +vol);
    }

    //strike price
    var k
    if ($("#mcb_k").val()==""){
      alert("Please input strike price");
      return
    }else{
      k = $("#mcb_k").val();
      //alert("Value: " +k);
    }

    //risk-free rate
    var r
    if ($("#mcb_r").val()==""){
      alert("Please input risk-free rate");
      return
    }else{
      r = $("#mcb_r").val();
      //alert("Value: " +r);
    }

    //time to maturity
    var t
    if ($("#mcb_t").val()==""){
      alert("Please input time to maturity");
      return
    }else{
      t = $("#mcb_t").val();
      //alert("Value: " +t);
    }

    //type
    var type
    if ($("#mcb_type").val()==""){
      alert("Please input option type");
      return
    }else{
      type = $("#mcb_type").val();
      //alert("Value: " +type);
    }

    //type
    var c_v
    if ($("#mcb_c_v").val()==""){
      alert("Please input Control Variate");
      return
    }else{
      c_v = $("#mcb_c_v").val();
      //alert("Value: " +type);
    }

    var rho
    if ($("#mcb_rho").val()==""){
      alert("Please input rho");
      return
    }else{
      rho = $("#mcb_rho").val();
      //alert("Value: " +type);
    }

    alert("begin to post data")

    $.post("/mcb",
      {
        mcb_s1: s1,
        mcb_s2: s2,
        mcb_vol1: vol1,
        mcb_vol2: vol2,
        mcb_I: I,
        mcb_c_v: c_v,
        mcb_k: k,
        mcb_r: r,
        mcb_t: t,
        mcb_rho: rho,
        mcb_type: type
      },

      function(data,status){
        //alert("Data: "+data+'\nStatus: '+status);
        $("#mcb_ans").text(data);
      });
    
    $("#mcb_ans").text('Calculating...');

      



    


  });

  $("#btn_bt_cal").click(function(){
    //asset value
    var s
    if ($("#bt_S").val()==""){
      alert("Please input asset value");
      return
    }else{
      s = $("#bt_S").val();
      //alert("Value: " +s);
    }

    //volatility
    var vol
    if ($("#bt_vol").val()==""){
      alert("Please input volatility");
      return
    }else{
      vol = $("#bt_vol").val();
      //alert("Value: " +vol);
    }

    //strike price
    var N
    if ($("#bt_N").val()==""){
      alert("Please input n");
      return
    }else{
      N = $("#bt_N").val();
      //alert("Value: " +k);
    }

    //strike price
    var k
    if ($("#bt_K").val()==""){
      alert("Please input strike price");
      return
    }else{
      k = $("#bt_K").val();
      //alert("Value: " +k);
    }

    //risk-free rate
    var r
    if ($("#bt_r").val()==""){
      alert("Please input risk-free rate");
      return
    }else{
      r = $("#bt_r").val();
      //alert("Value: " +r);
    }

    //time to maturity
    var t
    if ($("#bt_t").val()==""){
      alert("Please input time to maturity");
      return
    }else{
      t = $("#bt_t").val();
      //alert("Value: " +t);
    }

    //type
    var type
    if ($("#bt_type").val()==""){
      alert("Please input option type");
      return
    }else{
      type = $("#bt_type").val();
      //alert("Value: " +type);
    }

    alert("begin to post data")

    $.post("/bt",
      {
        bt_s: s,
        bt_vol: vol,
        bt_N: N,
        bt_k: k,
        bt_r: r,
        bt_t: t,
        bt_type: type
      },

      function(data,status){
        //alert("Data: "+data+'\nStatus: '+status);
        $("#bt_ans").text(data);
      });
    
    $("#bt_ans").text('Calculating...');

      



    


  });



});
