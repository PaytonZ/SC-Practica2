
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '1590606851186325',
      xfbml      : true,
      version    : 'v2.3'
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "//connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));


require([
        "esri/map",
        "dojo/query",
        "dojo/on", 
        "dojo/dom", 
        "esri/dijit/Search",
        "dojo/domReady!"

      ], function (Map, Search , query, on, dom) {
         var map = new Map("map", {
            basemap: "streets",
            center: [-3.69, 40.42], // lon, lat
            zoom: 7
         });

         var s = new Search({
            map: map
         }, "search");
         s.startup();
         
      // Wire UI Events
         on(dom.byId("btnStreets"),"click", function() { 
           map.setBasemap("streets");
         });
         on(dom.byId("btnSatellite"),"click", function() { 
           map.setBasemap("satellite");
         });
         on(dom.byId("btnHybrid"),"click", function() { 
           map.setBasemap("hybrid");
         });
         on(dom.byId("btnTopo"),"click", function() { 
           map.setBasemap("topo");
         });
         on(dom.byId("btnGray"),"click", function() { 
           map.setBasemap("gray");
         });
         on(dom.byId("btnNatGeo"),"click", function() { 
           map.setBasemap("national-geographic");
         });
         // Toggle panel
         on(dom.byId("chevron"), "click", function(e){
           if (query(".glyphicon.glyphicon-chevron-up")[0]) {
             query(".glyphicon").replaceClass("glyphicon-chevron-down","glyphicon-chevron-up");
             query(".panel-body.collapse").removeClass("in");
           } else {
             query(".glyphicon").replaceClass("glyphicon-chevron-up","glyphicon-chevron-down");
             query(".panel-body.collapse").addClass("in");
           }
         });

      });

