
class Denigma.MemberController extends Batman.Controller
  ###
    This controller contains basic grid events
  ###
  #fiels that are used in filtering
  fields: ['id','name','surname','organization','age','salary']


  model_name: "Member"
  page_size: 15
  scroll_threshold: 80 #when to load new portion of records

  with_pagination: (str)=>
    switch str
      when str==null then "?page_size=#{@page}"
      when str.contains? !str.contains("page_size") && str.contains("?") then str+"&page_size=#{@page}"
      else str

  model: => Denigma.get(@model_name)

  constructor: ->
    super
    @set "_items",undefined
    @newNovice()
    for f in @fields then @set(f,"")
    @addScrolling()


  clean: (node, event, context)->
    @newNovice()



  newNovice: ->
    ###
      prepares new model for creation
    ###
    @set "novice", new Denigma.Member()

  addScrolling: ->
    ###
      adds custom mscrolling to the grid
    ###
    callback = (e)=>
      if e.topPct>@scroll_threshold
        model = @model()
        if(model.page?)
          p = model.page
          unless p.loading==true
            if p.next?
              options = @with_pagination(p.next.substring(p.next.indexOf("?")+1)+"")
              fun = (err, records, env)->#console.log(records)
              model.load(options,fun)
              #model.load()
              p.loading = true
        else
          console.log("no scroll")


    params =
      theme:"dark-thick"
      advanced:
        updateOnContentResize: true
        autoScrollOnFocus: true
        updateOnBrowserResize:true
        autoHideScrollbar:true
        contentTouchScroll:true
      scrollButtons:
        enable: true
      callbacks:
        whileScrolling: callback

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


  add: (node, event, context)->
    ###
      creates new  model
      TODO: figure out what to do with id
    ###
    model = @get("novice")
    node = $(node).parent().parent()
    #node  = $(context.get("node"))
    #debugger
    @validate(model,node)
    model.save()
    unless model.get("errors").length>0 then @newNovice()

  validate: (model,node)->
    ###
        TODO: rewrite in less ugly way
    ###
    onerror = (e, errors)=>
      #errors = e.attribute for e in model.get("errors").toArray() when e.attribute?
      errors = e.attribute for e in model.get("errors").toArray() when e.attribute?
      for f in @fields
        fld = node.find(".#{f}")
        if errors!=[] and (f==errors or f in errors)
          fld.addClass("wrong")
        else
          fld.removeClass("wrong")
    model.validate(onerror)

  blur: (node, event, context) ->
    model = context.get("member")
    node  = $(context.get("node"))
    @validate(model,node)

  save: (node, event, context) ->
    ###
      saves model,
      TODO: rewrite in less ugly way
    ###
    model = context.get("member")
    node  = $(context.get("node"))
    @validate(model,node)

    model.save()

  remove: (node, event, context) ->
    ###
      saves model
    ###
    model = context.get("member")
    model.destroy()


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
        unless (v=="" or v==undefined) then return true
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