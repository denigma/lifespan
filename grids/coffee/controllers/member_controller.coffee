class Denigma.MemberController extends Batman.Controller
  ###
    This controller contains basic grid events
  ###
  #fiels that are used in filtering
  fields: ["id","name","surname","organization","age","salary"]

  constructor: ->
    super
    @set "_items",undefined
    @newNovice()
    for f in @fields then @set(f,"")
    @addScrolling()

  newNovice: ->
    @set "novice", new Denigma.Member()


  addScrolling: ->
    ###
      adds custom mscrolling to the grid
    ###
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

  add: ->
    ###
      creates new
    ###
    #new Denigma.Member.save({},)

  save: (node, event, context) ->
    ###
      saves model
    ###
    model = context.get("member")
    alert JSON.stringify(Denigma.Member.get("validators"))
    model.save()


  filter: (node, event, context) ->
    ###
      applies filtering to the grid
    ###
    #gets filtering options filled by use
    opts = @get("options")
    options = {}
    for key, val of opts
      if val!=undefined and val!=""
        options[key] = val
    #alert JSON.stringify(options)

    #updates the record in the grid
    callback = (err,records)=>
      #alert JSON.stringify(records)
      @set "_items", records
    Denigma.Member.load(options,callback)

  clear: (node, event, context) ->
    if(@get("filtered"))
      @set("options",{})
      @filter() #update models

  #accessor that tells us if any of fielter fields are filled
  @accessor 'filtered',
    get: ->
      unless @fields? then return false
      for f in @fields
        v = @get(f)
        unless (v=="" or v==undefined)
          return true
      false

  #accessor that gets values from filterinputs and generate options for Model.load()
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

#activates method of the contoller
Denigma.root("member#index")
