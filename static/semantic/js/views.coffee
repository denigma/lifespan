
#= extern Batman.View

class Batman.BetterView extends Batman.View
  ###
    this view is an alternative to Batman's default's one prodiving an ability to
  ###

  node: false
  options: null

  @register: (key,param)->
    ###
      as default option of Batman seems to be buggy I had to write my own function for that
      it stores key to be used for view creation
      on rendered values of all from data-view-{key} will be saved inside the view
    ###
    @::options?=new Batman.SimpleHash
    @::options.set key, param

  render: ->
    super
    @node = @get("node")
    fun = (key,param) =>
      path = "data-view-#{key}".toLowerCase()
      if @node.hasAttribute(path)
        attr = @node.getAttribute path
        @set(key,attr)
      else
        if param=="mandatory" then Batman.developer.error("there is no mandatory option #{key} for the view")
    @options.forEach(fun) if @options?

  keyCode:
    BACKSPACE: 8,
    COMMA: 188,
    DELETE: 46,
    DOWN: 40,
    END: 35,
    ENTER: 13,
    ESCAPE: 27,
    HOME: 36,
    LEFT: 37,
    NUMPAD_ADD: 107,
    NUMPAD_DECIMAL: 110,
    NUMPAD_DIVIDE: 111,
    NUMPAD_ENTER: 108,
    NUMPAD_MULTIPLY: 106,
    NUMPAD_SUBTRACT: 109,
    PAGE_DOWN: 34,
    PAGE_UP: 33,
    PERIOD: 190,
    RIGHT: 39,
    SPACE: 32,
    TAB: 9,
    UP: 38




class Batman.ChannelView extends Batman.BetterView
  ###
  View that is connected to some socket channel
  ###
  channelName: null
  channel: null

  @register("key","mandatory")

  connect: ->
    ###
      works with channel
    ###
    @channelName ?= @get "key"
    @channel = Batman.Socket.getInstance().getChannel(@channelName)

  render: ->
    super
    @connect()


#a view for tasks of this chat

#= extern Batman.View

class Denigma.UserView extends Batman.View
  constructor: ->
    # process arguments and stuff
    super
    #write node to separate variable, node is an HTMLNode to which view is attached to
    #$node = $ @get("node")


#a view for messages of this chat

#= extern Batman.View

class Denigma.MessageView extends Batman.View
  ###
    View for messages of this chat
  ###
  constructor: ->
    # process arguments and stuff
    super
    #writes node to separate variable, node is an HTMLNode to which view is attached to
    #@node = $ @get("node")

  render: ->
    super
    node = $ @get "node"
    node.hide().fadeIn("slow")

#a view for tasks of this chat

#= extern Batman.View


class Denigma.TaskView extends Batman.View
  constructor: ->
    # process arguments and stuff
    super

  render: ->
    super
    #node = $ @get "node"
    #node.fadeTo("slow",0.5)
    #write node to separate variable, node is an HTMLNode to which view is attached to
# @node = $ @get("node")
# @node.fadeTo("slow",0.5)
# @node.mouseover(->node.fadeTo("fast",0.8))
# @node.mouseout -> node.fadeTo("fast",0.5)
# @node.mousedown(->node.fadeTo("fast",1))




###
  In many cases we need to search with search suggessions, t
  he intention of this class if to provide such functionality
###



class Denigma.SearchBoard extends Batman.ChannelView

  @edit: null

  constructor: ->
    super
    @set("titles",new Batman.Set())
    @set("results",new Batman.Set())

  @register("result")
  @register("field")
  @register("input")



  lookupHandler: (event)=>
    ###
      fires when lookup info received
    ###
    tlt = @get("titles")
    tlt.clear()
    for t in event.content.list
      tlt.add(t)
    @set("titles",tlt) #just for 'overcheck'

  searchHandler: (event)=>
    ###
      fires when search resultsreceived
    ###
    @get("titles").clear()
    res = @get("results")
    res.clear()
    for r in event.content.list
      res.add(r)

  render: ->
    super
    node = $ @get("node")
    inp = "#"+@get("input")
    @edit = $(inp)
    @bind(@edit)

  connect: ->
    ###
      works with channel
    ###
    super
    #@channel.on("lookup", lookme)
    searchme = @searchHandler
    @channel.on "search", searchme


  @accessor "active",-> @get("query").length>0
  #@set("query","test")

  lookup: (newVal,oldVal)=>
    if @channel?
      field = @get "field"
      if(field?)
        @channel.lookup(field,newVal)
      else
        console.log "no field #{field}"
        @channel.query(newVal)
    else
      alert "no suggesssion channel!"

  split: (val) => val.split(" ") #/,\s*/

  extractLast: (term) =>  @split(term).pop() if term?

  look: (request, response) =>
    ###
      sends request to the channel
    ###
    #delegate back to autocomplete, but extract the last term
    term = @extractLast(request.term)
    field = @get "field"
    onceHandler = (event)=>
      lookme(event)
      titles = @get "titles"
      response(titles.toArray())

    @channel.lookup(field,term)
    lookme = @lookupHandler #assigment to overcome dreadful this javascript problem
    @channel.once "lookup", onceHandler

  focus:
    =>false

  select: (event, ui) =>
    ###
      fires when you selected the term
    ###
    newVal = ui.item.value
    s1 = newVal.indexOf("(")
    s2 = newVal.indexOf(")")

    if s1>1 and s2>s1
      name = newVal.substring(0,s1-1)
      value = newVal.substring(s1+1,newVal.length-1)
    else
      name = newVal
      value = newVal
    @edit.val(name)
    Denigma.fire "fisheye", value,"genesgraph" #make fishyey event to traverse the graph
    true



  multiSelect: (event, ui) =>
    value = @edit.val()
    terms = @split(value)
    newVal = ui.item.value
    # remove the current input
    terms.pop()
    # add the selected item
    terms.push newVal
    # add placeholder to get the comma-and-space at the end
    terms.push " "
    @edit.val(terms.join(" "))
    false


  keyDownHandler: (event)=>
      event.preventDefault()  if event.keyCode is $.ui.keyCode.TAB and $(this).data("ui-autocomplete").menu.active



  bind: (input)=>
    minLength = 2
    source = @look
    select = @select
    focus = @focus

    # don't navigate away from the field on tab when selecting an item
    input.bind("keydown", @keyDownHandler).autocomplete
      minLength:minLength
      delay: 300
      source: source
      select: select
      focus: focus



