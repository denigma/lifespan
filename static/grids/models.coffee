class Denigma.Text extends Batman.Model
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
