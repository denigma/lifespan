class Denigma.MemberController extends Batman.Controller

  _items: undefined

  fields: ["name","surname","organization","age","salary"]

  constructor: ->
    super
    for f in @fields then @set(f,"")
    @addScrolling()

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
    $("section.tbody").mCustomScrollbar(verParams)

    horParams = params
    horParams.horizontalScroll = true
    #$("#chatboard").mCustomScrollbar(horParams)

  index: ->

    #alert "Hello!"
    #@render(view: new Batman.View(html: '[<div data-yield="foo"></div>]'))

  out: (node, event, context)->
    ###
      fires when mouse went out of row
    ###
    node  = $(context.get("node"))
    node.removeClass("selected")

  over: (node, event, context)->
    ###
      fires when mouse is over  row
    ###
    node  = $(context.get("node"))
    node.addClass("selected")

  click: (node, event, context)->
    ###
      not yet used
    ###
    node  = context.get("node")
    $node = $(node)
    #$node.children().css('background-color', 'red')
    model = context.get("member")
    #debugger

  create: ->
    new Denigma.Member.save()

  save: (node, event, context) ->
    ###
      saves model
    ###
    model = context.get("member")
    model.save()


  filter: (node, event, context) ->
    opts = @get("options")
    options = {}
    for key, val of opts
      if val!=undefined and val!=""
        options[key] = val
    #alert JSON.stringify(options)

    callback = (err,records)=>
      #alert JSON.stringify(records)
      @set "_items", records
    Denigma.Member.load(options,callback)

  clear: (node, event, context) ->
    if(@get("filtered"))
      @set("options",{})
      @filter() #update models

  @set "_items",undefined
  @set "name", ""
  @set "surname", ""
  @set "organization", ""
  @set "age", ""
  @set "salary", ""

  #accessor that tells us if any of fielter fields are filled
  @accessor 'filtered',
    get: ->
      unless @fields? then return false
      for f in @fields
        v = @get(f)
        unless (v=="" or v==undefined)
          return true
      false

  @accessor 'options',
    get: ->
      res = {}
      for f in @fields
        res[f] = @get(f)
      return res

    set: (dic)->
      for f in @fields
        if f in dic
          v = dic[f]
          @set(f,v)
        else
          @set(f,"")

  @accessor 'items',
    get: ->
      vals = @get "_items"
      if vals==undefined then Denigma.get('Member.all') else vals

Denigma.root("member#index")
