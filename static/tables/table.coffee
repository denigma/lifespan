jQuery ->
  ###
  $.ajax
    url: '/data',
    dataType : "json",
    success:  (data, textStatus) -> alert JSON.stringify(data)
  ###
  d3.json('/data',(data)-> document.write(JSON.stringify(data)))
  ###
  {"pk":8,"model":"lifespan.member","fields":{"salary":7000,"organization":"Denigma","age":17,"surname":"surname_7","name":"username_7"}}
  ###

#class Denigma.Header extends Batman.Object

#class Denigma.Table
