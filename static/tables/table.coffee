Denigma.on "start", ->
  ###
    Event to initiate the main app
  ###
  Denigma.Table.main()

class Denigma.Model extends Batman

###
  [{"pk":1,"model":"lifespan.member","fields":{"salary":0,"organization":"Denigma","age":10,"surname":"surname_0","name":"username_0"}},
  {"pk":2,"model":"lifespan.member","fields":{"salary":1000,"organization":"Denigma","age":11,"surname":"surname_1","name":"username_1"}}
  ,{"pk":3,"model":"lifespan.member","fields":{"salary":2000,"organization":"Denigma","age":12,"surname":"surname_2","name":"username_2"}}]
###

class Denigma.Row extends Denigma.BasicView #TODO: complete

class Denigma.Table extends Denigma.Control

  constructor: (selector,subclass)->
    ###
      jquery-like selector string is passed,
      something like '#lifespan'
    ###
    super(selector,"tr",subclass)

  append: (novel)->
    novel.append("tr").data((d)-> [for key,value of d then key]).selectAll("td").append("td")


  update: (sel)->
    sel.selectAll("td").text((d,i)->(d[i]))

  draw: (data)->
    sel =  @select(data)
    @hide(sel.exit())
    novel = @append(sel.enter())
    @update(sel)

  select: (data)->
    @node.selectAll("table.#{@subclass}").data(data)

  parse: (data)->
    document.write(JSON.stringify(data))
    alert "does not work yet!"
    @draw(data)
    #vals = for item in data then item
    #item.fields if item.fields?
    #alert JSON.stringify(data)
    #mess = new Denigma.Message(id:"id",text:"sometext",user:"someuser")
    #mess.save()



  load: (uri)->
    fun = (data)=>@parse(data)
    d3.json(uri,fun)

  @main: ()->
    table = new Denigma.Table("table","member")
    table.load('/data')

class Denigma.Message extends Batman.Model
  ###
  model for messages
  contains text and user fields
  ###

  #@belongsTo('users', {name: "User"})

  @encode 'id','text', 'user'
  ###
    id and two other fields to be stored: text and user
    when you make models do not forget about id
  ###


  @validate 'text', presence: true
  ###
    validate if text is present each time we create Message
  ###


  @persist Batman.LocalStorage

  @storageKey: 'messages'
