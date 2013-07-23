Denigma.on "start", ->
  ###
    Event to initiate the main app
  ###
  Denigma.Table.main()

class Denigma.Table extends Denigma.Control

class Denigma.Row extends Denigma.BasicView

  append: (novel)->
    td = novel.selectAll("*.cell")
    td.data((d)->d).enter().append("div").attr("class","cell").text((d,i)->d)
    novel.selectAll("*.cell").text((d,i)->d)

  update: (sel)->#sel.selectAll("*.cell").text((d,i)->d).style("color","red")

class Denigma.Table extends Denigma.Control

  rows:null
  body: undefined

  constructor: (selector)->
    ###
      jquery-like selector string is passed,
      something like '#lifespan'
    ###
    super(selector,"*.row","grids")
    @body = @node.append("section")
    @body.attr("class","grids")
    @rows = new Denigma.Row()
    @addScrolling()


  append: (novel)->
    row = novel.append("section").attr("class","row")
    @rows.append(row)
    #tr.selectAll("td").style('background-color',"red")
    #td = tr.selectAll("td").data((d)->d).enter().append("td").text((d,i)->d)
    #td.enter().append("td").text("SOmetext")

  addScrolling: ->

    params =
      theme:"dark-thick"
      advanced:
        updateOnContentResize: true
        autoScrollOnFocus: true
        updateOnContentResize: true
        updateOnBrowserResize:true
        autoHideScrollbar:true
      scrollButtons:{
        enable: true
      }

    verParams = params
    $("#main").mCustomScrollbar(verParams)

    horParams = params
    horParams.horizontalScroll = true
    #$("#chatboard").mCustomScrollbar(horParams)

  update: (sel)->
    row = sel.select("section.row")
    row.selectAll("div").style('background-color',"red")

    row.style("background-color","red")
    #alert sel.data()
    @rows.update(row)

  draw: (data)->
    sel =  @select(data)
    @hide(sel.exit())
    novel = @append(sel.enter())
    @update(sel)

  select: (data)->  @body.selectAll("*.#{@subclass}").data(data)

  parse: (data)->
    #alert "does not work yet!"
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
    table = new Denigma.Table("#"+"main")
    table.load('data')