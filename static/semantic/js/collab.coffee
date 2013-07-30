###
# SocketEvent class #
Socket Event class is a class that does all conversions and packing of events send by sockets and channels
###

#= extern Batman.Object

class Batman.SocketEvent
  ###
  Socket Event class is a class that does all conversions and packing of events send by sockets and channels
  it contains a lot of useful static helpers to generate events that needed
  ###

  constructor: (@content, @channel, @request = "push", @room = "all")->
    ###
      creates websocket event where
      content is inside content variable, channel is for source (model) or type of content
      request is for what you want to do with content
      room is for what users to you want to spread this info
    ###
    unless @content.id? or @content.query then @content.id = SocketEvent.genId()
    #@id = if id=="" then SocketEvent.genId() else id



  @makeEvent: (content,channel, req, room = "all")->
    ###
      creates a socketevent, where:
      content is content of event
      channel is name of the channel that is used for this event
      req is a request with what this event is send
      room is an info to which users should the event be sent to
    ###
    new Batman.SocketEvent(content, channel, req, room)

  @makeQueryEvent: (query,channel, room = "all")->Batman.SocketEvent.makeEvent(query:query, channel, "read", room)

  @makeLookupEvent: (lField,lQuery,channel, room = "me")->
    content =
      field: lField
      query: lQuery
    Batman.SocketEvent.makeEvent(content, channel, "lookup", room)



  @makePushEvent: (content,channel, room = "all")->Batman.SocketEvent.makeEvent(content, channel, "push", room)

  @makeReadEvent: (id,channel, room = "all")->Batman.SocketEvent.makeEvent(id:id, channel, "read", room)

  @makeReadAllEvent: (channel,  room = "all")->Batman.SocketEvent.makeEvent(query:"all", channel, "read", room)

  @makeSaveEvent: (obj, channel)->
    data = Batman.SocketEvent.fromData(obj)
    data.channel = channel
    data.request = "save"
    data.room = "all"
    data


  @makeRemoveEvent: (id,channel, room="all")->Batman.SocketEvent.makeEvent(id:id, channel, "delete", room)



  @fromEvent: (event)->
    ###
    factory that generate SocketEvent from websocket event
    ###
    if event instanceof Batman.SocketEvent then return event
    if not event.data? then throw new Error("No data inside of websocket event")
    @fromData(event.data)

  @genId : ->
    ###
    ##Generates GUI as id for a record
    ###
    "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace /[xy]/g, (c) ->
      r = Math.random() * 16 | 0
      v = (if c is "x" then r else (r & 0x3 | 0x8))
      v.toString 16


  @fromData: (data)->
    ###
    factory that generate SocketEvent from the data
    ###
    if data instanceof Batman.SocketEvent then return data
    if typeof(data) =="string" then return @fromString(data)
    #to avoid typical bug of nested data
    data = data.data if data.data?
    channel = if data.channel? then data.channel else "default"
    content =
      if data.content?
        if typeof data.content =="string" then @toJSON(data.content) else data.content
      else
        data
    request = if data.request? then data.request else "push"
    room = if data.room? then data.room else "all"
    new Batman.SocketEvent(content,channel,request,room)


  @fromString: (str)->
    ###
    factory that generate SocketEvent from some string
    ###
    #if typeof str !="string" then throw new Error("not string received by fromString but "+JSON.stringify(str))
    data = @toJSON(str)
    return  if data is undefined or typeof(data)=="string" then new Batman.SocketEvent(str,"default","save") else @fromData(data)


  @toJSON = (str) ->
    ###
    tries to convert string to json, returns initial string if failed
    ###
    if typeof str !="string" then return str
    try
      obj = JSON.parse str
    catch e
      return str
    if obj==undefined then str else obj


###
# WorkerSocket class #
###

#= extern Batman.Object

class Batman.WorkerSocket extends Batman.Object
  ###
  #Worker socket#
  ###
  constructor: (worker)->
    if typeof(worker) =="string" then @worker = worker = new SharedWorker(worker)  else  @worker = worker
    @worker.port.onmessage = (e)=>@onmessage(e)
    @worker.port.onerror = (e)=>@onerror(e)
    Batman.container.worker =  @worker;
    @worker.port.start()
    Batman.WorkerSocket.instance = @

  @getInstance: (url="none")-> if Batman.WorkerSocket.instance? then Batman.WorkerSocket.instance else return new Batman.WorkerSocket(url)


  send: (obj)=>@worker.port.postMessage(obj)

  onopen: (i)->

  onerror: (error)->

  onmessage: (event)->
    data = if event.data? then event.data else event
    if data.ready? then onopen(data)

  onclose: ->

###
# MockSocket class #
Mock socket is needed for tests to simulate websocket behaviour
###

#= extern Batman.Object
#_require channel.coffee
#_require socket_event.coffee


class Batman.MockSocket extends Batman.Object
  ###
  #Mock socket#
  Mock socket is needed for tests to simulate websocket behaviour
  ###
  constructor: (@url)->
    super
    @onreceive = Batman.MockSocket.mockCallback(@)
    MockSocket.instance = @
    @onopen()

  @getInstance: (url="none")->if Batman.MockSocket.instance? then Batman.MockSocket.instance else return new Batman.MockSocket(url)

  isMock: true


  onreceive: (event)->event


  send: (event)=>@onreceive(event)

  onopen: ->
    ###
    Open event
    ###
    console.log "open"

  onmessage: (event)->
    ###
    On message
    ###
    data = event.data;

  onclose: =>
    console.log "close"

  randomInt: (min, max)=>
    ###
      random int generating function
    ###
    Math.floor(Math.random() * (max - min + 1)) + min

  @mockCallback:  (mock)=>
    ###
      this callback is needed to store data inside mock sockets and respond to read requests and other queirs
      NAPILNIK
    ###
    (event)=>
      #console.log event
      data = Batman.SocketEvent.fromString(event)
      #console.log data
      switch data.request
        when "save"
          ###
            if we received request to save something we answer to it with result
          ###
          data.request = "push"
          if data.content.id?
            id = data.content.id
            ###
              if we were give id we just give item with appropriate id
            ###
            mock.set id, data
            all = mock.getOrSet(data.channel, =>new Batman.SimpleSet())
            res = all.find (item)->item.id==id
            if res? then all.remove res
            all.add data.content
            mock.onmessage(data)
        when "delete"
          if data.content.id?
            id = data.content.id
            mock.unset id
            all = mock.getOrSet(data.channel, =>new Batman.SimpleSet())
            res = all.find (item)->item.id==id
            if res? then all.remove(res)
        when "read"
          if data.content.id?
            data = mock.get(data.content.id)
            data.request = "answer"
            mock.onmessage(data)
          else
            if data.content.query? and data.content.query=="all"
              col = mock.get(data.channel)
              if col? and col.length>0
                content = col.toArray()
                message = new Batman.SocketEvent(content, data.channel,"readAll")
                mock.onmessage(message)
              else
                mock.onmessage(new Batman.SocketEvent("_nil_", data.channel,"readAll"))


###
# MockSocket class #
Mock socket is needed for tests to simulate websocket behaviour
###

#= extern Batman.Object
#_require Batman.Channel
#_require Batman.SocketEvent



class Batman.CacheSocket extends Batman.Object

  isMock: true
  isCache: true
  input: []

  onopen: ->
    ###
    Open event
    ###
    console.log "open"

  constructor: (@url)->
    super
    @input = []

  send: (data)=> @input.push(data)

  onmessage: (event)->
    ###
    On message
    ###
    data = event.data
    console.log(data)

  onerror: =>
    console.log "error"

  onclose: =>
    console.log "close"

  randomInt: (min, max)=>
    ###
      random int generating function
    ###
    Math.floor(Math.random() * (max - min + 1)) + min

  unapply: (successor)=>
    if(@input? and successor.send?)
      for el in @input then successor.send(el)


###
  #Socket class#
  it not only uses either real or mock socket but broadcasts messages to various channels through events
###

#= extern Batman.Object
#_require socket_event
#_require cache_socket
#_require channel


class Batman.Socket extends Batman.Object
  ###
    websocket wrapper that broadcast info to its channels
    it not only uses either real or mock socket but broadcasts messages to various channels through events
  ###
  constructor: (url)->
    ###
    creates a socket object
    ###
    #checks if websocket is in batman container
    @router = new Batman.SimpleRouter()
    @websocket = @getWebSocket(url)
    Batman.Socket.instance = @



  url: "none"


  isMock: => not @websocket? or @websocket.isMock?

  createWebSocket:  (url)=>
    ###
      creates websocket or mocksocket
    ###
    if url=="none"
      websocket = new Batman.CacheSocket(url)
    else
      websocket = new WebSocket(url)
    @url = url
    @setWebsocket(websocket)

  setWebsocket: (websocket)=>
    defOpen = (event)=>
      @websocket = websocket
      @addSocketHandlers(@websocket)
    if @websocket?
      if websocket==@websocket then return @websocket
      if @websocket.isCache?
        old = @websocket
        websocket.onopen = (event)=>
          defOpen(event)
          old.unapply(websocket)
      else
        websocket.onopen = defOpen
    else
      websocket.onopen = defOpen
    if websocket.isMock? then websocket.onopen()

  addSocketHandlers: (websocket)=>
    websocket.onmessage = (event)=> @broadcast(event)
    websocket.onerror = (err)=>alert "some ERROR occured"
    websocket.onclose = ()=>alert "socket is CLOSED"
    websocket

  broadcast: (info)->@router.broadcast(info,@)


  getWebSocket: (url)=>
    ###
      TODO: rewrite, all this searches, the global scope only confuses
    ###
    if  Batman.container.websocket?
      if (Batman.container.websocket.isMock and url=='none') or url==@url
        return Batman.container.websocket
    @createWebSocket(url)




  withUrl: (url)=>
    ###
      returns self but changes the websocket if needed
    ###
    if(url!=@url) then @websocket = @getWebSocket(url)
    @


  @getInstance: (url="none")=>
    ###
      works as singletone
      TODO: rewrite
    ###
    if Batman.Socket.instance? then Batman.Socket.instance else return new Batman.Socket(url)
    ###
    if Batman.container.socket?
      return Batman.container.socket.withUrl(url)
    else
      return new Batman.Socket(url)

    ###

  getChannel: (name)=>
    ###
      gets or creates channel
    ###
    @getOrSet(name,=>new Batman.Channel(name).attach(@))

  getSpecialChannel: (name,factory)=>
    ###
      gets or creates channel with factory that is provided
    ###
    @getOrSet(name,=>factory().attach(@))


  getVideoChannel: (name,room)=>
    ###
      gets or creates video channel
    ###
    #TODO: think how to fix in Future
    @getOrSet(name+"2"+room,=>new Batman.VideoChannel(name,room).attach(@))



  send: (obj)=> @router.send(obj, @websocket)

  ask: (question)=>
    ###
      executes if there is a request to the router (but without info to be send to server)
    ###
    @router.respond(question,@)




###
# Channel class #
Every sockets info to channels.
Channels are needed to communicate directly with the model
###
#= extern Batman.Object




class Batman.Channel extends Batman.Object
  ###
  #Channel class
  Every sockets info to channels.
  Channels are needed to communicate directly with the model
  ###
  constructor: (name) ->
    @name = name
    @on "onmessage", (event)=>@onmessage(event)

  save: (obj, id) =>
    obj.id = id
    @save obj

  save: (obj)=> @fire "send", Batman.SocketEvent.makeSaveEvent(obj,@name)

  read: (id)=> @fire "send", Batman.SocketEvent.makeReadEvent(id, @name)

  readAll: => @fire "send", Batman.SocketEvent.makeReadAllEvent(@name)

  remove: (id)=> @fire "send", Batman.SocketEvent.makeRemoveEvent(id, @name)

  lookup: (field,query)=> @fire "send", Batman.SocketEvent.makeLookupEvent(field,query, @name)

  query: (query)=> @fire "send", Batman.SocketEvent.makeQueryEvent(query, @name)

  stream2src: (stream)=>
    ###
      gets URL from the stream
    ###
    if window.URL?
      window.URL.createObjectURL(stream)
    else
      if window.webkitURL?
        window.webkitURL.createObjectURL(stream)
      else
        if window.mozURL?
          window.mozURL.createObjectURL(stream)
        else
          stream

  askWebcam: =>
    @ask "webcam"



  send: (obj) =>
    data = Batman.SocketEvent.fromData(obj)
    data.channel = @name
    @fire "send", data


  receive: (event) =>
    #should receive event with data
    @fire "onmessage", event
    @fire(event.request, event)

  onNextMessage:(fun)=>@once "onmessage", (event)=>fun(event)

  onmessage: (event) =>
    ###
      call back the receives info from socket send to this channel
    ###

  ask: (question)=>
    ###
      asks router for some additional info
    ###
    @fire "ask", question


  attach: (obj)=>
    ###
      Attaches the channel to the socket wrapper and subscribes to its events
    ###
    receive = @receive #trick to overcome "this" javascript change
    obj.on @name, receive
    obj.on "all", receive

    send = obj.send
    @on "send", send

    @on "ask", obj.ask
    cl = @constructor.name
    obj.fire(cl,@name)
    @
###
  video channel class, temporal version
  will be refactored in the future
###





class Batman.VideoChannel extends Batman.Channel

  peer: null


  ###
    mystream is a temporal global variable to save a stream from a webcome
  ###

  constructor: (name, @room, @myStream = null)->
    super(name)
    @set("src","")
    #alert "name = #{name} | room = #{@room}"
    @startPeer()
    @on "ICE", (event)=>@onGetICE(event.content)
    @on "offer",  (event)=>@onGetOffer(event.content)
    @on "answer", (event)=>@onGetAnswer(event.content)


  askWebcam: =>
    @ask "webcam"

  startPeer: (servers=null)=>
    ###
    starts p2p connection
    ###
    @peer = @makePeer()
    @peer.onicecandidate = @onCreateICE
    @peer.onaddstream = @onGetRemoteStream





  makePeer:  (servers=null)=>
    if window.RTCPeerConnection?
      new RTCPeerConnection(servers)
    else
      if window.mozRTCPeerConnection?
        new mozRTCPeerConnection(servers)
      else
        new webkitRTCPeerConnection(servers)

  onWebCamSuccess:  (stream)=>
    ###
      when webcam stream received
    ###
    @myStream = stream
    @peer.onaddstream = (st)=>  #just for protection
    @peer.addStream(stream)
    @peer.onaddstream = @onGetRemoteStream
    @fire "localStream", stream



  call: =>
    ###
      Makes a call
    ###
    console.log "VideoChannel CALL from #{@name} 2 #{@room}"
    if @myStream?
      @peer.createOffer(@onCreateOffer)
    else
      @askWebcam()
      @on "localStream", @call


  onCreateOffer: (desc)=>
    ###
      fires when you propose and offer
    ###
    @peer.setLocalDescription(desc)
    offer = Batman.SocketEvent.makeEvent(desc,@name,"offer",@room)
    @fire "send", offer

  onGetOffer: (event)=>
    ###
      fires when you received another's offer
    ###
    desc = new RTCSessionDescription(event)
    @peer.setRemoteDescription(desc)
    @peer.createAnswer(@onCreateAnswer)
    console.log "offer received"



  onCreateAnswer:  (desc)=>
    ###
      fires when you created an answer
    ###
    @peer.setLocalDescription(desc)
    answer = Batman.SocketEvent.makeEvent(desc,@name,"answer",@room)
    @fire "send", answer

  onGetAnswer:  (event)=>
    ###
      fires when you received an answer
    ###
    desc = new RTCSessionDescription(event)
    @peer.setRemoteDescription(desc)
    console.log "answer received"

  onGetRemoteStream: (e)=>
    ###
      fires when you got stream
    ###
    console.log "got remote stream"
    if e.stream?
      stream = e.stream
      @fire "remoteStream", stream
    else
      alert "bug in onGetRemoteStream"

  onCreateICE: (event)=>
    ###
      fires when you make an ICE candidates
    ###
    if event.candidate?
      cand = event.candidate
      evt = Batman.SocketEvent.makeEvent(cand,@name,"ICE",@room)
      @fire "send", evt
    ###
    else
      alert "onICE do not work well"
      alert JSON.stringify(event)
    ###

  onGetICE: (event)=>
    ###
      fires when you received and ICE
    ###
    #cand = event.candidate?
    #str = JSON.stringify(event)
    #№alert "I got ice! "+str
    @peer.addIceCandidate(new RTCIceCandidate(event))

  ###
  onmessage: (event)=>
    switch event.request
      when "ICE" then @onGetICE(event.content)
      when "offer" then  @onGetOffer(event.content)
      when "answer" then @onGetAnswer(event.content)
  ###

  onError: (e)->
    alert "There has been a problem retrieving the streams - did you allow access?"

  subscribeLocal: (vid)=>
    @on "localStream", (stream)=>
      src = @stream2src(stream)
      @set "src", src
      vid.src = src

  subscribeRemote: (vid)=>
    @on "remoteStream", (stream)=>
      src = @stream2src(stream)
      @set "src", src
      vid.src = src

  attach: (obj)=>
    ###
      Attaches the channel to the socket wrapper and subscribes to its events
    ###
    receive = @receive #trick to overcome "this" javascript change
    if @room? and @room!="all" #TODO: fix this Indus-like code in Future
      obj.on(@name+"2"+@room,receive)
    else
      obj.on @name, receive
    obj.on "all", receive

    send = obj.send
    @on "send", send

    @on "ask", obj.ask
    cl = @constructor.name
    obj.fire(cl,@name)
    @

  attach: (obj)=>
    onStream = @onWebCamSuccess
    obj.on "localStream", onStream
    super(obj)
    if @myStream?
      @peer.addStream(@myStream)
      @peer.onaddstream = @onGetRemoteStream
    else
      @askWebcam()
    @


class Batman.VideoSlotChannel extends Batman.Channel

  channels: null

  OPEN_PEERS: "openpeers"
  PEERS_OPENED: "peersopened"

  CALL_PEERS: "callpeers"
  PEERS_CALLED: "peerscalled"

  CLOSE_PEERS: "closepeers"
  PEERS_CLOSED: "peersclosed"


  ###
    mystream is a temporal global variable to save a stream from a webcome
  ###
  constructor: (name, @room)->
    super(name)
    @channels = new Batman.SimpleHash()
    @on @OPEN_PEERS , (event)=>@peersOpened(event)
    @on @CALL_PEERS , (event)=>@peersCalled(event)


  peersOpened: (event)=>
    ###
      fires when we received peers to be created
    ###
    console.log("PEERS OPENED: "+JSON.stringify(event))
    unless event.content then console.log "no content"
    cont = event.content
    if not (cont.from? or cont.to)  then console.log "no from or to"
    socket = Batman.Socket.getInstance()
    for f in cont.from
      h = @channels.getOrSet(f, =>new Batman.SimpleHash())
      for t in cont.to
        console.log("open video channel from #{f} to #{t}")
        ch = h.getOrSet(t,=>socket.getVideoChannel(f,t))
        ch.on "localStream", (stream)=> @fire "local", @stream2src(stream)
        ch.on "remoteStream", (stream)=>
          src = @stream2src(stream)
          console.log "#{@name}: remoteSRC = #{src}"
          @fire "remote", src

    event.content.name = @PEERS_OPENED
    event.request = @PEERS_OPENED
    event.room = @room
    @send event
    @fire(@PEERS_OPENED)


  peersCalled: (event)=>
    ###
      fires when we received peers to be created
    ###
    console.log("PEERS CALLED: "+JSON.stringify(event))
    unless event.content then console.log "no content"
    cont = event.content
    if not (cont.from? or cont.to)  then console.log "no from or to"
    socket = Batman.Socket.getInstance()
    for f in cont.from
      h = @channels.getOrSet(f, =>new Batman.SimpleHash())
      for t in cont.to
        console.log("call video channel from #{f} to #{t}")
        ch = h.getOrSet(t,=>socket.getVideoChannel(f,t))
        ch.call()
    event.content.name = @PEERS_CALLED
    event.request = @PEERS_CALLED
    event.room = @room
    @send event
    @fire(@PEERS_CALLED)

  call: =>
    req = "broadcast"
    evt = new Batman.SocketEvent(req, @name, req, @room)
    @fire "send", evt



  open: =>
    req = "video"
    content =
      name: req
    evt = new Batman.SocketEvent(content, @name, req, @room)
    @fire "send", evt


  onError: (e)->
    alert "There has been a problem with slot channel?"
###
  Routerclass
###

#= extern Batman.Object


class Batman.SimpleRouter extends Batman.Object
  ###
    Simple router does only simple broadcasting relying on channel info from the socket
  ###

  broadcast: (info, socket)->
    ###
      transforms info into SocketEvents and routes them further, to the channels
      some routers split info into several parts and send to difference channels
    ###
    event = Batman.SocketEvent.fromEvent(info)
    ### broadcasts the message further ###
    unless event instanceof Batman.SocketEvent
      throw Error 'should be socket event'
    ### broadcast event to appropriate channels ###
    socket.fire(event.channel, event)
    if(event.room? and event.room!="all")
      socket.fire(event.channel+"2"+event.room, event)  #TODO: fix this indus code


  send: (obj, websocket)->
    ###
      sends event to the websocket
    ###
    if typeof obj == 'string'
      websocket.send(obj)
    else
      str = JSON.stringify Batman.SocketEvent.fromData(obj)
      websocket.send str
      #websocket.send obj

  myStream: null
  webCamPending: false


  respond: (question,socket)->
    ###
      respond to questions from channels
    ###
    switch question
      when "webcam"
        if @myStream?
          socket.fire "localStream", @myStream
        else
          if @webCamPending==false
            navigator.getUserMedia or (navigator.getUserMedia = navigator.mozGetUserMedia or navigator.webkitGetUserMedia or navigator.msGetUserMedia)
            if navigator.getUserMedia
              onsuccess = (stream)=>
                socket.fire "localStream", stream
                @webCamPending = false
              onerror = @onError
              @webCamPending = true
              navigator.getUserMedia
                video: true
                audio: true
                onsuccess
                onerror
            else
              alert "getUserMedia is not supported in this browser."
          @webCamPending = true


###
  Chat router class
###



class Batman.ChatRouter extends Batman.SimpleRouter

  broadcast: (info, socket)->
    ###
      routes events to the chat
    ###
    #if not info.data? then throw new Error("no data inside event cannot route further")
    unless info.data? then return super(info,socket)

    if info.data.content? then return super(info,socket)
    data = Batman.SocketEvent.toJSON(info.data)
    if data.kind?
      switch data.kind
        when "join"
          @addUser(data,socket)
          @message(data,socket)

        when "quit"
          @removeUser(data,socket)
          @message(data,socket)

        when "talk"  then @message(data,socket)
        when "message" then @message(data,socket)

  addUser: (data,socket) ->
    content =
      id:data.user
      name:data.user
    event = new Batman.SocketEvent.makePushEvent(content,"users")
    socket.fire "users", event

  removeUser: (data,socket) -> socket.fire "users", Batman.SocketEvent.makeRemoveEvent(data.user,"users")

  message: (data,socket) ->
    text = if data.message? then data.message else data.text
    content =
      "user": data.user
      "text": text
    event = Batman.SocketEvent.makePushEvent(content,"messages")
    socket.fire "messages", event

  task: (data,socket) ->
    content =
      "user": data.user
      "title": data.title
    event = Batman.SocketEvent.makePushEvent(content,"tasks")
    socket.fire "tasks", event



  send: (obj, websocket)->
    ###
      sends event to the websocket
    ###
    #return super(obj, websocket)
    if typeof obj == 'string'
      websocket.send(obj)
    else
      event = Batman.SocketEvent.fromData(obj)
      if event.channel =="messages"
        if event.content?
          if event.content.text?
            event.text = event.content.text
          else
            if event.content.data?
              event.text = event.content.data
            else event.text = event.content
      str = JSON.stringify Batman.SocketEvent.fromData(obj)
      websocket.send str
      #websocket.send obj




###
#SocketStorage#

This is a Socket storage adaptor needed to connect Batman's models to websocket
It has not been finished yet.
###

#= extern Batman.Object

#_require ./socket_event.coffee
#_require ./channel.coffee
#_require ./socket.coffee
#_require ./mock_storage.coffee

class Batman.SocketStorage extends Batman.StorageAdapter
  ###
  #SocketStorage#

  This is a Socket storage adaptor needed to connect Batman's models to websocket
  It has not been finished yet.
  ###

  constructor: (model) ->
    ###
      Initialize storage adaptor as well as socket
    ###
    super(model)
    @socket = new Batman.Socket.getInstance()

  _dataMatches: (conditions, data) ->
    match = true
    for k, v of conditions
      if data[k] != v
        match = false
        break
    match

  subscribe: (model)->
    ###
      Subscribe model to different events
      subscribe function is called after readall
    ###
    channel = @socket.getChannel(model.storageKey)
    if model.primaryKey?
      key = model.primaryKey
    else
      key = "id"

    #TODO: rewrite addition because it changes the order of elements
    channel.on "push", (event)=>
      all = model.get("loaded")
      res = all.find (item)->
        item.get(key)== event.content[key]
      all.remove(res)
      record = @getRecordFromData(event.content, model)
      all.add(record)
    channel.on "delete", (event)=>
      all = model.get("loaded")
      res = all.find (item)->
        item.get(key)== event.content[key]
      all.remove(res)
    channel


  readAll: (env, next) ->#@skipIfError (env, next) ->
    ###
    overrided readAll to add subscription
    TODO: what to do with subscriptions if readALL is called several times?
    ###
    channel = @subscribe(env.subject)
    options = env.options.data

    channel.onNextMessage (event)->
      try
        records = []
        if event.content? and event.content.length?

           for item in event.content
             records.push item if @_dataMatches(options,item)

        env.recordsAttributes = records
      catch error
        env.error = error
      next()
    channel.readAll()


  create: ({key,id, recordAttributes}, next) -> #@skipIfError ({channel,id, recordAttributes}, next) ->
    channel = @socket.getChannel(key)
    channel.save(recordAttributes,id)
    next()

  read: ({key,id, recordAttributes}, next) -> #@skipIfError ({key,id, recordAttributes}, next) ->
    channel = @socket.getChannel(key)
    channel.onNextMessage =>
      if !env.recordAttributes
        env.error = new @constructor.NotFoundError()
        next()
    channel.read(id)
    #do not forget about change in future


  update: ({key,id, recordAttributes}, next) ->#@skipIfError ({key,id, recordAttributes}, next) ->
    channel = @socket.getChannel(key)
    channel.save(recordAttributes,id)
    next()

  destroy: ({key,id}, next) -> #@skipIfError ({key,id}, next) ->
    channel = @socket.getChannel(key)
    channel.remove(id)
    next()


  @::before 'read', 'create', 'update', 'destroy', @skipIfError (env, next) ->
    if env.action == 'create'
      env.id = env.subject.get('id') || env.subject._withoutDirtyTracking => env.subject.set('id', Batman.SocketEvent.genId())
    else
      env.id = env.subject.get('id')

    unless env.id? then env.error = new @constructor.StorageError("Couldn't get/set record primary key on #{env.action}!")
    key = @storageKey(env.subject)
    env.key = key

    next()


  @::before 'create', 'update', @skipIfError (env, next) ->
    env.recordAttributes = JSON.stringify(env.subject)
    next()

  @::after 'read', @skipIfError (env, next) ->
    if typeof env.recordAttributes is 'string'
      try
        env.recordAttributes = @_jsonToAttributes(env.recordAttributes)
      catch error
        env.error = error
        return next()
    env.subject._withoutDirtyTracking -> @fromJSON env.recordAttributes
    next()

  @::after 'read', 'create', 'update', 'destroy', @skipIfError (env, next) ->
    env.result = env.subject
    next()

  @::after 'readAll', @skipIfError (env, next) ->
    env.result = env.records = for recordAttributes in env.recordsAttributes
      @getRecordFromData(recordAttributes, env.subject)
    next()


